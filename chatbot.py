"""
AI Course Assistant Chatbot
A rule-based chatbot that answers FAQs about AI courses and programming
"""

import re
from datetime import datetime


class CourseAssistantBot:
    """
    A simple rule-based chatbot for answering course-related questions.
    Uses keyword matching and pattern recognition to identify user intents.
    """
    
    def __init__(self):
        """Initialize the chatbot with predefined responses"""
        self.name = "AI Course Assistant"
        self.intents = {
            'greeting': {
                'patterns': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon'],
                'responses': [
                    "Hello! I'm your AI Course Assistant. How can I help you today?",
                    "Hi there! Ask me anything about AI courses and programming.",
                    "Greetings! I'm here to help with your AI course questions."
                ]
            },
            'course_info': {
                'patterns': ['course', 'what is dai011', 'programming for ai', 'subject', 'module'],
                'responses': [
                    "DAI011: Programming for AI is a course that teaches Python programming fundamentals with a focus on AI and ML applications. You'll learn data handling, basic algorithms, and how to use AI libraries.",
                    "This course covers Python basics, data analysis with Pandas, machine learning with scikit-learn, and building simple AI applications."
                ]
            },
            'assessment': {
                'patterns': ['cat', 'exam', 'assessment', 'test', 'marks', 'grade', 'evaluation'],
                'responses': [
                    "The course assessment includes Continuous Assessment Tests (CATs) worth 30% and a final exam worth 70%. CAT 2 focuses on GitHub workflow and a Python AI project.",
                    "Your CAT 2 is worth 20% of continuous assessment (40 marks total). It includes GitHub setup, a Python project, and documentation."
                ]
            },
            'libraries': {
                'patterns': ['library', 'libraries', 'package', 'pandas', 'numpy', 'scikit', 'tools'],
                'responses': [
                    "Common AI/ML libraries in Python include: Pandas (data manipulation), NumPy (numerical computing), scikit-learn (machine learning), Matplotlib (visualization), and TensorFlow/PyTorch (deep learning).",
                    "For this course, you'll mainly use Pandas for data analysis, NumPy for arrays, and scikit-learn for basic machine learning models."
                ]
            },
            'help_project': {
                'patterns': ['help', 'project', 'assignment', 'stuck', 'how to', 'guide'],
                'responses': [
                    "For your project: 1) Set up GitHub repository, 2) Choose a project option (chatbot, data analyzer, or ML model), 3) Write clean, commented code, 4) Document everything with screenshots. Need help with a specific part?",
                    "I can help! Break your project into small steps: start with GitHub setup, then write basic code, test it, commit changes regularly, and finally write your report with screenshots."
                ]
            },
            'github': {
                'patterns': ['github', 'git', 'repository', 'commit', 'push', 'version control'],
                'responses': [
                    "GitHub is a platform for version control using Git. Basic workflow: 1) git add (stage files), 2) git commit -m 'message' (save changes), 3) git push (upload to GitHub). Make at least 3 commits showing your progress!",
                    "For CAT 2, create a public repository named 'AI_Programming_Project', add a README, and commit your code incrementally with clear messages like 'Initial setup', 'Added data handling', 'Final implementation'."
                ]
            },
            'thanks': {
                'patterns': ['thank', 'thanks', 'appreciate', 'helpful'],
                'responses': [
                    "You're welcome! Good luck with your project!",
                    "Happy to help! Feel free to ask if you have more questions.",
                    "Glad I could assist! Best wishes with your coursework!"
                ]
            },
            'goodbye': {
                'patterns': ['bye', 'goodbye', 'see you', 'exit', 'quit'],
                'responses': [
                    "Goodbye! Good luck with your studies!",
                    "See you later! Feel free to come back anytime.",
                    "Take care! All the best with your AI projects!"
                ]
            }
        }
        
        self.conversation_history = []
    
    def preprocess_input(self, user_input):
        """
        Clean and normalize user input for better matching
        
        Args:
            user_input (str): Raw user input
            
        Returns:
            str: Cleaned lowercase input
        """
        # Convert to lowercase and remove extra spaces
        cleaned = user_input.lower().strip()
        # Remove punctuation except spaces
        cleaned = re.sub(r'[^\w\s]', '', cleaned)
        return cleaned
    
    def identify_intent(self, user_input):
        """
        Identify the user's intent based on keyword matching
        
        Args:
            user_input (str): Preprocessed user input
            
        Returns:
            str: Identified intent key or 'unknown'
        """
        for intent, data in self.intents.items():
            for pattern in data['patterns']:
                if pattern in user_input:
                    return intent
        return 'unknown'
    
    def generate_response(self, intent):
        """
        Generate appropriate response based on identified intent
        
        Args:
            intent (str): Identified user intent
            
        Returns:
            str: Bot response
        """
        if intent == 'unknown':
            return ("I'm not sure I understand. I can help with: course information, "
                   "assessments, Python libraries, project guidance, and GitHub. "
                   "Try asking about any of these topics!")
        
        # Return the first response for simplicity (you could randomize)
        return self.intents[intent]['responses'][0]
    
    def chat(self, user_input):
        """
        Main chat function that processes input and generates response
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Bot's response
        """
        # Store conversation
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.conversation_history.append({
            'time': timestamp,
            'user': user_input,
        })
        
        # Process input
        cleaned_input = self.preprocess_input(user_input)
        intent = self.identify_intent(cleaned_input)
        response = self.generate_response(intent)
        
        # Store bot response
        self.conversation_history[-1]['bot'] = response
        self.conversation_history[-1]['intent'] = intent
        
        return response
    
    def get_statistics(self):
        """
        Get chatbot usage statistics
        
        Returns:
            dict: Statistics about the conversation
        """
        intent_counts = {}
        for entry in self.conversation_history:
            intent = entry.get('intent', 'unknown')
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        return {
            'total_messages': len(self.conversation_history),
            'intent_distribution': intent_counts
        }


def main():
    """
    Main function to run the chatbot in terminal
    """
    print("=" * 60)
    print("🤖 AI COURSE ASSISTANT CHATBOT")
    print("=" * 60)
    print("\nWelcome! I can answer questions about:")
    print("  • Course information (DAI011)")
    print("  • Assessments and grading")
    print("  • Python libraries for AI")
    print("  • Project guidance")
    print("  • GitHub and version control")
    print("\nType 'quit' or 'exit' to end the conversation.")
    print("=" * 60)
    print()
    
    # Initialize chatbot
    bot = CourseAssistantBot()
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit command
        if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
            print(f"\n{bot.name}: Goodbye! Good luck with your studies! 👋\n")
            
            # Display statistics
            stats = bot.get_statistics()
            print("\n" + "=" * 60)
            print("📊 CONVERSATION STATISTICS")
            print("=" * 60)
            print(f"Total messages: {stats['total_messages']}")
            print("\nIntent distribution:")
            for intent, count in stats['intent_distribution'].items():
                print(f"  • {intent}: {count}")
            print("=" * 60)
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Get and display bot response
        response = bot.chat(user_input)
        print(f"\n{bot.name}: {response}\n")


if __name__ == "__main__":
    main()