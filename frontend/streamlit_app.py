import streamlit as st
import requests
import json
import os

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

st.title("🤝 Personalized Networking Assistant")
st.write("Generate AI-powered networking conversation starters and verify facts.")

# =====================================================
# Conversation Starter Generator
# =====================================================

st.header("🎯 Generate Conversation Starters")

event_description = st.text_area("Enter Event Description")
user_interests = st.text_input("Your Interests (comma separated)")

if st.button("Generate Conversation Starters"):

    if event_description and user_interests:

        payload = {
            "description": event_description,
            "interests": [i.strip() for i in user_interests.split(",")]
        }

        try:
            response = requests.post(
                f"{BASE_URL}/analyze",
                json=payload
            )

            if response.status_code == 200:

                result = response.json()

                topics = result.get("topics", [])

                st.session_state["topics"] = topics

                st.success("Conversation starters generated successfully!")

                os.makedirs("database", exist_ok=True)

                history_file = "database/history.json"

                history = []

                if os.path.exists(history_file):
                    try:
                        with open(history_file, "r") as f:
                            history = json.load(f)
                    except:
                        history = []

                history.append({
                    "event": event_description,
                    "interests": payload["interests"],
                    "generated": topics
                })

                with open(history_file, "w") as f:
                    json.dump(history, f, indent=4)

            else:
                st.error(response.text)

        except Exception as e:
            st.error(e)

    else:
        st.warning("Please enter both event description and interests.")

# =====================================================
# Generated Results
# =====================================================

if "topics" in st.session_state:

    st.divider()
    st.header("📋 Generated Results")

    for topic in st.session_state["topics"]:
        st.success(topic)

    st.subheader("Feedback")

    feedback_file = "database/feedback.json"

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Like"):

            feedback = []

            if os.path.exists(feedback_file):
                try:
                    with open(feedback_file, "r") as f:
                        feedback = json.load(f)
                except:
                    feedback = []

            for topic in st.session_state["topics"]:
                feedback.append({
                    "suggestion": topic,
                    "feedback": "like"
                })

            with open(feedback_file, "w") as f:
                json.dump(feedback, f, indent=4)

            st.success("Feedback saved successfully!")

    with col2:
        if st.button("👎 Dislike"):

            feedback = []

            if os.path.exists(feedback_file):
                try:
                    with open(feedback_file, "r") as f:
                        feedback = json.load(f)
                except:
                    feedback = []

            for topic in st.session_state["topics"]:
                feedback.append({
                    "suggestion": topic,
                    "feedback": "dislike"
                })

            with open(feedback_file, "w") as f:
                json.dump(feedback, f, indent=4)

            st.info("Feedback saved successfully!")

# =====================================================
# Wikipedia Fact Verification
# =====================================================

st.divider()

st.header("📚 Wikipedia Fact Verification")

topic = st.text_input("Enter Topic to Verify")

if st.button("Verify Fact"):

    if topic:

        try:

            response = requests.post(
                f"{BASE_URL}/fact-check",
                json={"topic": topic}
            )

            if response.status_code == 200:

                result = response.json()

                st.success(result.get("status"))
                st.write(result.get("summary"))

            else:
                st.error(response.text)

        except Exception as e:
            st.error(e)

    else:
        st.warning("Please enter a topic.")

# =====================================================
# Conversation History
# =====================================================

st.divider()

st.header("🕒 Conversation History")

if st.button("Show History"):

    history_file = "database/history.json"

    if os.path.exists(history_file):

        try:

            with open(history_file, "r") as f:
                history = json.load(f)

            if history:

                for item in reversed(history):

                    st.markdown("---")

                    st.write("### Event")
                    st.write(item["event"])

                    st.write("### Interests")
                    st.write(", ".join(item["interests"]))

                    st.write("### Generated Topics")

                    for topic in item["generated"]:
                        st.write("•", topic)

            else:
                st.info("No history available.")

        except:
            st.info("History file is empty.")

    else:
        st.info("No history file found.")

# =====================================================
# Feedback History
# =====================================================

st.divider()

st.header("📝 Feedback History")

if st.button("Show Feedback"):

    feedback_file = "database/feedback.json"

    if os.path.exists(feedback_file):

        try:

            with open(feedback_file, "r") as f:
                feedback = json.load(f)

            if feedback:

                for item in reversed(feedback[-10:]):

                    icon = "👍" if item["feedback"] == "like" else "👎"

                    st.write(f"{icon} {item['suggestion']}")

            else:
                st.info("No feedback available.")

        except:
            st.info("Feedback file is empty.")

    else:
        st.info("No feedback file found.")