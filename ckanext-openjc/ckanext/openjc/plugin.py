import ckan.plugins as plugins


class OpenJcPlugin(plugins.SingletonPlugin):
	def update_config(self, config):
		config['extra_template_paths'] = 'ckanext-openjc/templates'
