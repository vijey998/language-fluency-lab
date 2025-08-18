#pragma once
#include <list>
#include <optional>
#include <queue>
#include <unordered_map>
namespace scheduler {
template<class T> class StablePriorityQueue {
 // TODO: nested Entry, comparator, priority_queue, sequence number.
public:
 void push(T value,int priority);
 T pop();
 [[nodiscard]] bool empty() const;
};
// Implement LruCache<K,V> using list + unordered_map of iterators.
// Implement BoundedQueue<T> using mutex + condition_variable + close semantics.
}
