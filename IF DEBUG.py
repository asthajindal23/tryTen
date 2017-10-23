if DEBUG:
	MEDIA_URL = '/media/'
	STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
	MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
	STATICFILES_DIRS=(
	os.path.join(os.path.dirname(BASE_DIR), "static", "static")
	)