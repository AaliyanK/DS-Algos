def mergeArray(nums1,nums2):
    i = 0 # Indices
    j = 0
    len1 = len(nums1) # 4
    len2 = len(nums2) # 5
    finalArr = []

    while ((i<len1) and (j<len2)):
        if nums1[i] > nums2[j]:
            finalArr.append(nums2[j])
            j += 1
        else:
            finalArr.append(nums1[i])
            i += 1
    
    # For remaining elements: i continually increases
    while i < len1:
        finalArr.append(nums1[i])
        i +=1
    
    while j < len2:
        finalArr.append(nums2[j])
        j +=1




    return finalArr

print(mergeArray([1,4,9,10], [2,3,6,7,8]))