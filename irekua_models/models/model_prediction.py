from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from irekua_database.models import Annotation


class ModelPrediction(Annotation):
    model_version = models.ForeignKey(
        'ModelVersion',
        on_delete=models.PROTECT,
        db_column='model_version_id',
        verbose_name=_('model version'),
        help_text=_('Model and version used for this prediction'),
        blank=False,
        null=False)
    certainty = models.FloatField(
        db_column='certainty',
        verbose_name=_('certainty'),
        help_text=_('Model certainty of prediction. A number from 0 to 1.'),
        blank=False,
        null=False)

    class Meta:
        verbose_name = _('Model Prediction')
        verbose_name_plural = _('Model Predictions')
        ordering = ['-modified_on']

    def __str__(self):
        msg = _('Prediction of item %(item_id)s by model %(model)s')
        params = dict(item_id=self.item, model=self.model_version)
        return msg % params

    def clean(self):
        model = self.model_version.model
        try:
            model.validate_item_type(self.item.item_type)
        except ValidationError as error:
            raise ValidationError({'item': error})

        try:
            model.validate_event_type(self.event_type)
        except ValidationError as error:
            raise ValidationError({'event_type': error})

        annotation_type = self.model_version.model.annotation_type
        if annotation_type != self.annotation_type:
            raise ValidationError({
                'annotation_type': (
                    'Annotation type of annotation and model do not coincide '
                    f'({self.annotation_type} != {annotation_type})'
                )
            })

        super().clean()
