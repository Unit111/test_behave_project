import json
from datetime import datetime

from behave.model import Scenario
from behave.runner import Context


def after_scenario(context: Context, scenario: Scenario):
    save_report(context, scenario)


def save_report(context: Context, scenario: Scenario):
    # Initialize the report dictionary
    context.report = dict()
    # Save the name of the scenario
    context.report["name"] = scenario.name
    # Save the feature name
    context.report["feature"] = scenario.feature.name
    # Save the scenario status
    context.report["status"] = scenario.status.name
    # Save the scenario steps
    context.report["steps"] = [step.name for step in scenario.all_steps]
    # Save the scenario tags
    context.report["tags"] = scenario.effective_tags
    # Save the duration of the scenario
    context.report["duration"] = scenario.duration
    # Indicate if a hook has failed
    context.report["hook_failed"] = scenario.hook_failed
    # Save the scenario filename
    context.report["file"] = scenario.filename
    # Save the step with error if any
    context.report["failed_step"] = [step.name for step in scenario.all_steps if step.error_message is not None] or None
    # Save error message if any
    context.report["error_message"] = \
        [step.error_message for step in scenario.all_steps if step.error_message is not None] or None

    date_time = datetime.now().strftime("%Y_%m_%d_%H_%M")
    file_name = scenario.name.replace(" ", "_")

    with open('reports/{name}_{time}.json'.format(name=file_name, time=date_time), 'w') as outfile:
        json.dump(context.report, outfile)
