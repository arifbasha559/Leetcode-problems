class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int i = 0;
         while (true) {
            if (arr[i] < arr[i + 1]) {
                i++;
            } else {
                return i;
            }
        }
    }
};