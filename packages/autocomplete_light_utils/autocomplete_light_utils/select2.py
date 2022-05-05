from django.conf import settings
from django import forms

from dal import autocomplete


I18N_PATH = 'autocomplete_light/i18n/'


class CustomModelSelect2(autocomplete.ModelSelect2):

    # class Media:
    #     css = {
    #         'screen': ('css/custom_autocomplete.css',)
    #     }

    # @property
    # def media(self):
    #     base_media = super().media
    #     custom_media = forms.Media(css={'screen': ('css/custom_autocomplete.css',)})
    #     # return base_media + custom_media
    #     res = base_media + custom_media
    #     print(res._css_lists)
    #     return res

    @property
    def media(self):
        """Return JS/CSS resources for the widget."""
        extra = '' if settings.DEBUG else '.min'
        i18n_name = self._get_language_code()
        i18n_file = (
            '%s%s.js' % (I18N_PATH, i18n_name),
        ) if i18n_name else ()

        return forms.Media(
            js=(
                'admin/js/vendor/select2/select2.full.js',
                'autocomplete_light/autocomplete_light%s.js' % extra,
                'autocomplete_light/select2%s.js' % extra,
            ) + i18n_file,
            css={
                'screen': (
                    'admin/css/vendor/select2/select2%s.css' % extra,
                    'admin/css/autocomplete.css',
                    'autocomplete_light/select2.css',
                    'css/custom_autocomplete.css',
                ),
            },
        )
