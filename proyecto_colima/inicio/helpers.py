import os

def get_upload_path(instance, filename):
	try:
		try:
			index = filename.index('.')
			_filename = filename[index:]
		except:
			_filename = ''

		__filename = repr(instance).split(':')[0].strip('<')+'_'+str(instance.id)+_filename
	except:
		ruta = os.path.join(instance.REPOSITORIO, "%s" % filename)
	else:
		ruta = os.path.join(instance.REPOSITORIO, "%s" % __filename)

	return ruta