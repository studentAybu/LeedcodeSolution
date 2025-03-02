package LeedcodeSolution;

public class Merge_array_java {
   
        public int[] merge(int[] nums1, int m, int[] nums2, int n) {
            int[] numsMarge = new int[m + n];
            int i = 0, j = 0, k = 0;
     
     
            for (; i < m && j < n; k++) {
                if (nums1[i] <= nums2[j]) {
                    numsMarge[k] = nums1[i++];
                } else {
                    numsMarge[k] = nums2[j++];
                }
            }
     
     
            for (; i < m; i++, k++) {
                numsMarge[k] = nums1[i];
            }
     
     
            for (; j < n; j++, k++) {
                numsMarge[k] = nums2[j];
            }
     
     
            for (int index = 0; index < m + n; index++) {
                nums1[index] = numsMarge[index];
            }
            return numsMarge;
        }
     }
     
     
     

