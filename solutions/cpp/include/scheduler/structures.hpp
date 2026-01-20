#pragma once
#include <condition_variable>
#include <list>
#include <mutex>
#include <optional>
#include <queue>
#include <stdexcept>
#include <unordered_map>
namespace scheduler {
template<class T> class StablePriorityQueue {
 struct Entry { int priority; std::size_t seq; T value; };
 struct Compare { bool operator()(Entry const&a,Entry const&b)const{return a.priority==b.priority?a.seq>b.seq:a.priority<b.priority;} };
 std::priority_queue<Entry,std::vector<Entry>,Compare> q_; std::size_t seq_{};
public: void push(T value,int priority){q_.push({priority,seq_++,std::move(value)});} T pop(){if(q_.empty())throw std::out_of_range("empty"); auto v=std::move(const_cast<Entry&>(q_.top()).value);q_.pop();return v;} [[nodiscard]] bool empty()const{return q_.empty();}
};
template<class K,class V> class LruCache {
 using Node=std::pair<K,V>; std::size_t cap_; std::list<Node> items_; std::unordered_map<K,typename std::list<Node>::iterator> index_;
public: explicit LruCache(std::size_t c):cap_(c){if(!c)throw std::invalid_argument("capacity");} std::optional<V> get(K const&k){auto it=index_.find(k);if(it==index_.end())return std::nullopt;items_.splice(items_.begin(),items_,it->second);return it->second->second;} void put(K k,V v){if(auto it=index_.find(k);it!=index_.end()){it->second->second=std::move(v);items_.splice(items_.begin(),items_,it->second);return;} items_.emplace_front(std::move(k),std::move(v));index_[items_.front().first]=items_.begin();if(items_.size()>cap_){index_.erase(items_.back().first);items_.pop_back();}}
};
template<class T> class BoundedQueue {
 std::queue<T> q_; std::size_t cap_; bool closed_{}; std::mutex m_; std::condition_variable cv_;
public: explicit BoundedQueue(std::size_t c):cap_(c){} void push(T v){std::unique_lock lock(m_);cv_.wait(lock,[&]{return q_.size()<cap_||closed_;});if(closed_)throw std::runtime_error("closed");q_.push(std::move(v));cv_.notify_all();} std::optional<T> pop(){std::unique_lock lock(m_);cv_.wait(lock,[&]{return !q_.empty()||closed_;});if(q_.empty())return std::nullopt;T v=std::move(q_.front());q_.pop();cv_.notify_all();return v;} void close(){std::lock_guard lock(m_);closed_=true;cv_.notify_all();}
};
}
