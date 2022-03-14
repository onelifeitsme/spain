from haystack import indexes

# from planning.models import Schedule, EISPlacingRequest, PPG
# from purchases.models import NoticeVersion, RequestMessageStageHistory
from applications.objects.models import RentObject, DetailAndFeatureType


class ObjectIndex(indexes.SearchIndex, indexes.Indexable):
    content = indexes.CharField(document=True, use_template=True)
    category = indexes.CharField(model_attr='category', null=True)
    name = indexes.CharField(model_attr='name', null=True)
    type_of_deal = indexes.CharField(model_attr='type_of_deal', null=True)
    price = indexes.IntegerField(model_attr='price', null=True)
    country = indexes.CharField(model_attr='country', null=False)
    city = indexes.CharField(model_attr='city', null=True)
    amenities = indexes.MultiValueField()
    bedrooms = indexes.MultiValueField()
    details_and_features = indexes.MultiValueField()

    def prepare_amenities(self, obj):
        return [amenite.pk for amenite in obj.amenities.all()]

    def prepare_details_and_features(self, obj):
        return [i.pk for i in obj.detailandfeature_set.all()]

    def prepare_bedrooms(self, obj):
        try:
            detail_and_feature = obj.detailandfeature_set.filter(
                type=DetailAndFeatureType.objects.filter(name='Bedrooms'))
            if detail_and_feature:
                return [detail.property for detail in detail_and_feature[0].pk]
            else:
                return False
        except:
            return False

    # location = indexes.CharField(model_attr='location', null=True)
    # version = indexes.CharField(model_attr='version')
    # company_name = indexes.CharField(
    #     model_attr='created_by__company__company_name'
    # )
    # fin_kbk = indexes.BooleanField()
    # fin_kvr = indexes.BooleanField()
    # all_ppg_count = indexes.IntegerField(model_attr='all_ppg_count')
    # year_from = indexes.IntegerField(model_attr='year')
    # year_to = indexes.IntegerField(model_attr='year')
    # epr_updated_at = indexes.DateTimeField(null=True)
    # updated_at = indexes.DateTimeField(model_attr='updated_at', null=True)
    # publish_date_from = indexes.DateTimeField(model_attr='approved_at', null=True)
    # publish_date_to = indexes.DateTimeField(model_attr='approved_at', null=True)
    # is_purchase_center = indexes.BooleanField()
    # is_purchase_joint = indexes.BooleanField()
    # is_public_comment = indexes.BooleanField()
    # is_purchase_medications = indexes.BooleanField()

    def get_model(self):
        return RentObject

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


    # def prepare_fin_kbk(self, obj):
    #     for i in obj.ppg_set.all():
    #         for y in i.sourceoffinancing_set.all():
    #             if len(y.name) > 3:
    #                 return True
    #     return False
    #
    # def prepare_fin_kvr(self, obj):
    #     for i in obj.ppg_set.all():
    #         for y in i.sourceoffinancing_set.all():
    #             if len(y.name) <= 3:
    #                 return True
    #     return False
    #
    # def prepare_is_purchase_center(self, obj):
    #     return obj.ppg_set.filter(is_purchase_center=True).exists()
    #
    # def prepare_epr_updated_at(self, obj):
    #     eis_history = EISPlacingRequest.objects.filter(
    #         eis_placing_schedule=obj,
    #         status=EISPlacingRequest.SUCCESS
    #     )
    #     if eis_history.exists():
    #         return eis_history.last().updated_at
    #     return None
    #
    # def prepare_is_purchase_joint(self, obj):
    #     return obj.ppg_set.filter(is_purchase_joint=True).exists()
    #
    # def prepare_is_public_comment(self, obj):
    #     return obj.ppg_set.filter(is_public_comment=True).exists()
    #
    # def prepare_is_purchase_medications(self, obj):
    #     return NoticeVersion.objects.filter(
    #         notice__ppg__schedule=obj, is_purchase_medications=True
    #     ).exists()

