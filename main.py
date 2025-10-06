# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "dotenv",
#     "openai-agents",
# ]
# ///


from agents import Agent, ModelSettings, Runner, set_tracing_disabled
from dotenv import load_dotenv
from openai.types.shared import Reasoning


def main() -> None:
    set_tracing_disabled(True)
    load_dotenv()

    agent = Agent(
        name="sample-agent",
        instructions="You are a helpful assistant.",
        model="gpt-5-mini",
        model_settings=ModelSettings(
            reasoning=Reasoning(effort="minimal"),
        ),
    )

    first_prompt = "tell me an interesting fact"
    print(f"user: {first_prompt}")
    first_result = Runner.run_sync(agent, first_prompt)
    print(f"assistant: {first_result.final_output}")
    print()

    second_prompt = "tell me another"
    input = first_result.to_input_list() + [{"role": "user", "content": second_prompt}]
    print(f"user: {second_prompt}")
    second_result = Runner.run_sync(agent, input)
    print(f"assistant: {second_result.final_output}")
    print()


if __name__ == "__main__":
    main()
