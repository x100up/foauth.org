from oauthlib.oauth2.draft25 import utils
import foauth.providers


def token_uri(service, token, r):
    params = [((u'access_token', token)), ((u'api_key', service.client_id))]
    r.url = utils.add_params_to_uri(r.url, params)
    return r


class Disqus(foauth.providers.OAuth2):
    # General info about the provider
    provider_url = 'http://disqus.com/'
    docs_url = 'http://disqus.com/api/docs/'
    category = 'Social'

    # URLs to interact with the API
    authorize_url = 'https://disqus.com/api/oauth/2.0/authorize/'
    access_token_url = 'https://disqus.com/api/oauth/2.0/access_token/'
    api_domain = 'disqus.com'

    available_permissions = [
        (None, 'access your contact info'),
        ('write', 'access your contact info and add comments'),
        ('admin', 'access your contact info, add comments and moderate your forums'),
    ]
    permissions_widget = 'radio'

    bearer_type = token_uri

    def get_scope_string(self, scopes):
        return ','.join(scopes)

    def get_user_id(self, key):
        r = self.api(key, self.api_domain, u'/api/3.0/users/details.json')
        return r.json[u'response'][u'id']
