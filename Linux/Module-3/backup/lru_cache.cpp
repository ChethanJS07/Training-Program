#include <iostream>
#include <map>
using namespace std;

class Node {
public:
    int key;
    int val;
    Node *prev;
    Node *next;

    Node(int key, int val) {
        this->key = key;
        this->val = val;
        this->prev = nullptr;
        this->next = nullptr;
    }
};

class LRUCache {
private:
    map<int, Node*> mpp;
    int capacity;
    Node *head, *tail;

    // Helper methods as private member functions
    void insertAfterHead(Node *node) {
        Node *currAfterHead = head->next;
        head->next = node;
        node->prev = head;
        node->next = currAfterHead;
        currAfterHead->prev = node;
    }

    void deleteNode(Node *node) {
        Node *prevNode = node->prev;
        Node *nextNode = node->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
    }

    void removeAndDeleteTail() {
        if (tail->prev == head) return; // Empty list
        
        Node *nodeToDelete = tail->prev;
        deleteNode(nodeToDelete);
        mpp.erase(nodeToDelete->key);
        delete nodeToDelete; // Free memory
    }

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
        // Create dummy head and tail nodes
        head = new Node(-1, -1);  // Dummy head
        tail = new Node(-1, -1);  // Dummy tail
        head->next = tail;
        tail->prev = head;
        mpp.clear();
    }

    ~LRUCache() {
        // Clean up all nodes including head and tail
        Node* current = head;
        while (current) {
            Node* next = current->next;
            delete current;
            current = next;
        }
    }

    int get(int key) {
        if (mpp.find(key) == mpp.end()) {  // Key not found
            return -1;
        }
        
        Node *node = mpp[key];
        // Move to front (most recently used)
        deleteNode(node);
        insertAfterHead(node);
        
        return node->val;
    }

    void put(int key, int value) {
        if (mpp.find(key) != mpp.end()) {  // Key exists
            Node *node = mpp[key];
            node->val = value;  // Update value
            deleteNode(node);
            insertAfterHead(node);
        } else {  // New key
            if (mpp.size() == capacity) {
                removeAndDeleteTail();  // Remove least recently used
            }
            
            Node *node = new Node(key, value);
            mpp[key] = node;
            insertAfterHead(node);
        }
    }

    // Optional: Helper method to print cache (for debugging)
    void printCache() {
        cout << "Cache (MRU to LRU): ";
        Node* current = head->next;
        while (current != tail) {
            cout << "(" << current->key << ":" << current->val << ") ";
            current = current->next;
        }
        cout << endl;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int capacity;
    cin >> capacity;

    LRUCache cache(capacity);
    
    cout << "Testing LRU Cache with capacity " << capacity << ":\n";
    
    cache.put(1, 1);
    cache.put(2, 2);
    cout << "get(1): " << cache.get(1) << endl;  // returns 1
    cache.put(3, 3);  // evicts key 2
    cout << "get(2): " << cache.get(2) << endl;  // returns -1 (not found)
    cache.put(4, 4);  // evicts key 1
    cout << "get(1): " << cache.get(1) << endl;  // returns -1 (not found)
    cout << "get(3): " << cache.get(3) << endl;  // returns 3
    cout << "get(4): " << cache.get(4) << endl;  // returns 4

    return 0;
}
