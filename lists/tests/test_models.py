from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError

FRIST_ITEM = '첫 번째 아이템'
SECOND_ITEM = '두 번째 아이템'

class ListAndItemModelTest(TestCase):
    
    def add_item(self, list_, item_name):
        my_item = Item()
        my_item.list = list_
        my_item.text = item_name
        my_item.save()
    
    def test_saving_and_retrieving_items(self):
        list_ = List.objects.create()
            
        self.add_item(list_, FRIST_ITEM)
        self.add_item(list_, SECOND_ITEM)

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, FRIST_ITEM)
        self.assertEqual(first_saved_item.list, list_)

        second_saved_item = saved_items[1]
        self.assertEqual(second_saved_item.text, SECOND_ITEM)
        self.assertEqual(second_saved_item.list, list_)

    def test_connot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
            
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id))
        
        