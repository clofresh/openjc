import ckan.plugins as plugins


class OpenJcPlugin(plugins.SingletonPlugin):
	def update_config(self, config):
		plugins.toolkit.add_template_directory(config, 'templates')
