import os
from dotenv import load_dotenv
from utils.file_saver import save_study_plan

load_dotenv()

from agents.topic_builder import TopicBuilderAgent
from agents.ms_learn_module_picker import MSLearnModulePickerAgent
from agents.study_plan_generator import StudyPlanGeneratorAgent

# Azure AI Foundry credentials
API_KEY = os.getenv("AZURE_API_KEY")
BASE_URL = os.getenv("AZURE_FOUNDRY_URL")
MODEL = os.getenv("AZURE_MODEL")

# User input
USER_GOAL = """
I want to become an Azure AI Engineer in 3 months.
I know basic Python and I've used Azure VMs before but that's it.
I can study around 8-10 hours every week.
"""


def main():
    # Step 1: Topic Builder
    print("=" * 50)
    print("STEP 1: Topic Builder Agent")
    print("=" * 50)
    topic_agent = TopicBuilderAgent(api_key=API_KEY, base_url=BASE_URL, model=MODEL)
    topics = topic_agent.run(USER_GOAL)
    print(topics)
    print()

    # Step 2: MS Learn Module Picker
    print("=" * 50)
    print("STEP 2: MS Learn Module Picker Agent")
    print("=" * 50)
    module_agent = MSLearnModulePickerAgent(api_key=API_KEY, base_url=BASE_URL, model=MODEL)
    modules = module_agent.run(topics)
    print(modules)
    print()

    # Step 3: Study Plan Generator
    print("=" * 50)
    print("STEP 3: Study Plan Generator Agent")
    print("=" * 50)
    plan_agent = StudyPlanGeneratorAgent(api_key=API_KEY, base_url=BASE_URL, model=MODEL)
    study_plan = plan_agent.run(modules, USER_GOAL)
    print(study_plan)
    print()

    # Save to file
    save_study_plan(study_plan)
    print("✅ Study plan saved!")


if __name__ == "__main__":
    main()