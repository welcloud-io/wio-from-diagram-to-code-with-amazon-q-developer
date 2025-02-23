#!/usr/bin/env python3
from aws_cdk import App
from stacks.feedback_stack import FeedbackStack

app = App()
FeedbackStack(app, "FeedbackStack")
app.synth()