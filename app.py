#!/usr/bin/env python3

from aws_cdk import core

from cdk_python_project.cdk_python_project_stack import CdkPythonProjectStack

app = core.App()
CdkPythonProjectStack(app, "CdkPythonProjectStack")

app.synth()
