#include <iostream>
using namespace std;
class Node 
{
 
    public:
    int data;
    Node* next;
    Node(int data, Node* ptr = nullptr){
        this->data = data;
        this->next = ptr;
    }

    int return_data(){
        return this->data;
    }
    Node* return_next(){
        return next;
    }
    void set_next(Node* node){
        next = node;
    }
};

class LL 
{
    public:
    Node* head;
    LL()
    {
        this->head = nullptr;  
    }

    void addToStart (int data)
    {
        if (head != nullptr)
        {   
            Node * temp = new Node(data, head);
            head = temp;
        }
        else
        {
            Node * temp = new Node(data, nullptr);
            head = temp;
        }
    }

    void addToEnd(int data)
    {
        Node* temp = head;
        while (temp->return_next() != nullptr)
        {
            temp = temp->return_next();
        }
        Node* element = new Node(data, nullptr);
        temp->next = element;
    }

    void printAll()
    {
        Node * temp = head;
        while (temp != nullptr)
        {
            cout << temp->return_data()<<endl;
            temp = temp->return_next();
        }
    }
}; 


