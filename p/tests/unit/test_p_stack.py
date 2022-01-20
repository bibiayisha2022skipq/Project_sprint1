import aws_cdk as core
import aws_cdk.assertions as assertions

from p.p_stack import PStack

# example tests. To run these tests, uncomment this file along with the example
# resource in p/p_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PStack(app, "p")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
