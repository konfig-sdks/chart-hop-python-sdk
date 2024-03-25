from chart_hop_python_sdk.paths.oauth_token.post import ApiForpost
from chart_hop_python_sdk.paths.oauth_token.delete import ApiFordelete


class OauthToken(
    ApiForpost,
    ApiFordelete,
):
    pass
