from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError

class ListAndItemModelTest(TestCase):
    
    def add_item(self, list_, item_name):
        my_item = Item()
        my_item.list = list_
        my_item.text = item_name
        my_item.save()
    
    def test_saving_and_retrieving_items(self):
        list_ = List.objects.create()
            
        self.add_item(list_, '첫 번째 아이템')
        self.add_item(list_, '두 번째 아이템')

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.text, '첫 번째 아이템')
        self.assertEqual(first_saved_item.list, list_)

        second_saved_item = saved_items[1]
        self.assertEqual(second_saved_item.text, '두 번째 아이템')
        self.assertEqual(second_saved_item.list, list_)

    def test_connot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()