
@dataclass
class User:
        login: str
        id: str
        node_id: str
        avatar_url: str
        gravatar_id: str
        url: str
        html_url: str
        followers_url: str
        following_url: str
        gists_url: str
        starred_url: str
        subscriptions_url: str
        organizations_url: str
        repos_url: str
        events_url: str
        received_events_url: str
        type: str
        site_admin: str


def decoder(obj):
    return User(**obj)


result = json.loads(DATA, object_hook=decoder)
