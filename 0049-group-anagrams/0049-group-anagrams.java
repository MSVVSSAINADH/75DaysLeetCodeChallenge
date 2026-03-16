class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> hm = new HashMap<>();
        for(String st: strs)
        {
            char[] ch = st.toCharArray(); //converts the string to char arr
            Arrays.sort(ch);

            String word = new String(ch); //converts the char arr back to string

            if(!hm.containsKey(word))
            {
                hm.put(word, new ArrayList<>());    //creates a seperate list to store values
            }

            hm.get(word).add(st);   //add value into existing one
        }
        return new ArrayList<>(hm.values()); // return the list of values in hm
    }
}