import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_python_project.cdk_python_project_stack import CdkPythonProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_python_project/cdk_python_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonProjectStack(app, "cdk-python-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
