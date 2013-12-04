import ckan.plugins as plugins


class OpenJcPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    def update_config(self, config):
        plugins.toolkit.add_template_directory(config, 'templates')
