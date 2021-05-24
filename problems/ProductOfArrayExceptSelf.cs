// Runtime: 276 ms, faster than 68.89% of C# online submissions for Product of Array Except Self.
// Memory Usage: 39.2 MB, less than 85.51% of C# online submissions for Product of Array Except Self.

public class Solution {

    public int[] ProductExceptSelf(int[] nums) {

        int len = nums.Length;
        int[] output = new int[len];
        output[0] = 1;
        for (int i = 1; i < len; i++)
        {
            output[i] = nums[i - 1] * output[i - 1];
        }

        int r = 1;
        for (int i = len-1; i >= 0; i--)
        {
            output[i] = output[i] * r;
            r = r * nums[i];
        }
        return output;

    }

}