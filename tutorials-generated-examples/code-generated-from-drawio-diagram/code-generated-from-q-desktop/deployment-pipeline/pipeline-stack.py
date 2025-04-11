from aws_cdk import (
    Stack,
    aws_codebuild as codebuild,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as pipeline_actions,
    SecretValue,
    Environment
)
from constructs import Construct

class DeploymentPipelineStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the pipeline
        pipeline = codepipeline.Pipeline(
            self, "DeploymentPipeline",
            pipeline_name="CDK-Deployment-Pipeline"
        )

        # Source stage - GitHub
        source_output = codepipeline.Artifact()
        source_action = pipeline_actions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner="<YOUR_GITHUB_OWNER>",
            repo="<YOUR_GITHUB_REPO>",
            branch="main",
            oauth_token=SecretValue.secrets_manager("github-token"),
            output=source_output
        )

        # Add source stage
        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action]
        )

        # Create CodeBuild project for CDK deployment
        cdk_build = codebuild.PipelineProject(
            self, "CDKBuild",
            build_spec=codebuild.BuildSpec.from_object({
                "version": "0.2",
                "phases": {
                    "install": {
                        "commands": [
                            "npm install -g aws-cdk",
                            "pip install -r requirements.txt"
                        ]
                    },
                    "build": {
                        "commands": [
                            "cdk deploy --require-approval never"
                        ]
                    }
                }
            }),
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.STANDARD_5_0,
                privileged=True
            )
        )

        # Build stage
        build_output = codepipeline.Artifact()
        build_action = pipeline_actions.CodeBuildAction(
            action_name="CDK_Deploy",
            project=cdk_build,
            input=source_output,
            outputs=[build_output]
        )

        # Add build stage
        pipeline.add_stage(
            stage_name="Deploy",
            actions=[build_action]
        )
