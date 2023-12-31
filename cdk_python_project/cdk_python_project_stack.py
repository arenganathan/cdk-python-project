from aws_cdk import core
from aws_cdk import aws_s3 as _s3

class CdkPythonProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myBucket",
            bucket_name="cdkpythonprojectptack-sathish0101",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkPythonProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
