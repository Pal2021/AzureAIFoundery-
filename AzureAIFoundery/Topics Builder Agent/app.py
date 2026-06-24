import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

from agents.topic_builder import TopicBuilderAgent
from agents.ms_learn_module_picker import MSLearnModulePickerAgent
from agents.study_plan_generator import StudyPlanGeneratorAgent

st.set_page_config(page_title="MS Learn Path Builder", page_icon="🎯")
st.title("🎯 MS Learn Path Builder")

API_KEY = os.getenv("AZURE_API_KEY")
BASE_URL = os.getenv("AZURE_FOUNDRY_URL")
MODEL = os.getenv("AZURE_MODEL")

with st.form("learning_goal"):
    goal = st.text_input("What do you want to learn?", "Azure AI Engineer")
    experience = st.text_area("Your background", "Basic Python, used Azure VMs")
    hours = st.slider("Hours per week", 1, 40, 10)
    timeline = st.text_input("Target timeline", "3 months")
    submitted = st.form_submit_button("Generate My Path")

if submitted:
    user_input = f"Goal: {goal}\nExperience: {experience}\nHours: {hours}\nTimeline: {timeline}"

    # Step 1: Topics with streaming
    st.subheader("📚 Step 1: Topics")
    topic_agent = TopicBuilderAgent(api_key=API_KEY, base_url=BASE_URL, model=MODEL)
    
    # Create empty container for streaming
    topic_container = st.empty()
    full_text = ""
    
    for chunk in topic_agent.llm.generate_stream(user_input):
        full_text += chunk
        topic_container.markdown(full_text)
    
    # Step 2: Modules with streaming
    st.subheader("🔗 Step 2: MS Learn Modules")
    module_agent = MSLearnModulePickerAgent(api_key=API_KEY, base_url=BASE_URL, model=MODEL)
    
    module_container = st.empty()
    full_modules = ""
    
    for chunk in module_agent.llm.generate_stream(full_text):
        full_modules += chunk
        module_container.markdown(full_modules)
    
    # Step 3: Study Plan with streaming
    st.subheader("📅 Step 3: Study Plan")
    plan_agent = StudyPlanGeneratorAgent(api_key=API_KEY, base_url=BASE_URL, model=MODEL)
    
    plan_container = st.empty()
    full_plan = ""
    
    for chunk in plan_agent.llm.generate_stream(full_modules + "\n" + user_input):
        full_plan += chunk
        plan_container.markdown(full_plan)
    
    # Download button
    st.download_button("📥 Download", full_plan, "study_plan.md")
    st.success("✅ Done!")