class ReformatTheString {

    public static void main(String[] args) {
		String reformat = reformat("ab123");
		System.out.println(reformat);
    }
    
    public static String reformat(String s) {
        StringBuilder answer= new StringBuilder();
        
        ArrayList<Character> letter = new ArrayList<>();
        ArrayList<Character> digit = new ArrayList<>();
        
        // letter, digit 각각 저장
        for(int i=0; i<s.length(); i++) {
        	char charAt = s.charAt(i);
        	
        	if('0'<=charAt && charAt<='9') digit.add(charAt);
        	else letter.add(charAt);
        }
        
        // 케이스에 따라 분류
        if(letter.size()+1==digit.size()) {
        	for(int i=0; i<s.length(); i++) {
        		if(i%2==1) answer.append(letter.remove(0));
        		else answer.append(digit.remove(0));
        	}
        } else if(digit.size()+1==letter.size()) {
        	for(int i=0; i<s.length(); i++) {
        		if(i%2==1) answer.append(digit.remove(0));
        		else answer.append(letter.remove(0));
        	}
        } else if(digit.size()==letter.size()) {
        	if('0'<=s.charAt(0) && s.charAt(0)<='9') {
        		answer.append(letter.remove(0));
        		
        		for(int i=1; i<s.length(); i++) {
            		if(i%2==1) answer.append(digit.remove(0));
            		else answer.append(letter.remove(0));
            	}
        	} else {
        		answer.append(digit.remove(0));
        		
        		for(int i=1; i<s.length(); i++) {
            		if(i%2==1) answer.append(letter.remove(0));
            		else answer.append(digit.remove(0));
            	}
        	}
        }
        
        return answer.toString();
    }
}