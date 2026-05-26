/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* newLL = &dummy;
        
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;

        while (curr1 != nullptr && curr2 != nullptr)
        {
            if (curr1->val > curr2->val) 
            {
                newLL->next = curr2;
                curr2 = curr2->next;
            }
            else
            {
                newLL->next = curr1;
                curr1= curr1->next;
            }
            newLL = newLL->next;
        }
        if (curr1 != nullptr)
        {
            newLL->next = curr1;
        }
        else
        {
            newLL->next = curr2;
        }

        
        return dummy.next;
    }
};
