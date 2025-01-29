import streamlit as st

def main():
    st.title("Vulnerability Analysis Quiz")
    st.markdown("This quiz will test your understanding of vulnerability analysis concepts, including types of assessments, lifecycle phases, and risk assessment calculations.")

    questions = [
        {
            "question": "What is the primary purpose of vulnerability analysis?",
            "options": [
                "To exploit system weaknesses",
                "To identify security flaws in systems/applications",
                "To monitor network traffic",
                "To create penetration testing reports"
            ],
            "answer": "To identify security flaws in systems/applications",
            "explanation": "Vulnerability analysis aims to discover weaknesses in an environment, helping organizations manage their vulnerabilities."
        },
        {
            "question": "Passive vulnerability assessment involves actively sending requests to live systems.",
            "options": ["True", "False"],
            "answer": "False",
            "explanation": "Passive assessment uses packet sniffing and does not actively send requests."
        },
        {
            "question": "Which of the following are common sources of vulnerabilities in network systems? (Select all that apply)",
            "options": [
                "Open services",
                "Default configurations",
                "Misconfigurations"
            ],
            "answer": ["Open services", "Default configurations", "Misconfigurations"],
            "explanation": "These issues can lead to security weaknesses that attackers may exploit."
        },
        {
            "question": "What are the phases of the vulnerability management lifecycle?",
            "options": [
                "Assessment, Remediation, Verification, Monitoring",
                "Discovery, Exploitation, Reporting",
                "Planning, Implementation, Maintenance",
                "Analysis, Design, Development"
            ],
            "answer": "Assessment, Remediation, Verification, Monitoring",
            "explanation": "These phases help organizations manage their vulnerabilities effectively."
        },
        {
            "question": "What is SLE in risk assessment?",
            "options": [
                "Single Loss Expectancy",
                "Standard Loss Evaluation",
                "Systematic Loss Estimation",
                "Safe Loss Expectancy"
            ],
            "answer": "Single Loss Expectancy",
            "explanation": "SLE represents the expected monetary loss from a single incident."
        },
        {
            "question": "Which phase ensures that all vulnerabilities in the environment are eliminated?",
            "options": [
                "Monitoring Phase",
                "Remediation Phase",
                "Verification Phase",
                "Assessment Phase"
            ],
            "answer": "Verification Phase",
            "explanation": "The verification phase confirms that all known vulnerabilities have been addressed."
        },
        {
            "question": "What does ARO stand for?",
            "options": [
                "Annual Rate of Occurrence",
                "Average Rate of Occurrence",
                "Actual Rate of Occurrence",
                "Assumed Rate of Occurrence"
            ],
            "answer": "Annual Rate of Occurrence",
            "explanation": "'ARO' quantifies how often a risk is expected to occur in a year."
        },
        {
            "question": 'What is the purpose of creating a baseline in vulnerability management?',
            'options': [
                'To establish a reference point for security measures',
                'To identify new assets added to the network',
                'To assess external threats',
                'To monitor network traffic'
            ],
            'answer': 'To establish a reference point for security measures',
            'explanation': 'Creating a baseline helps in assessing changes and vulnerabilities over time.'
        },
        {
           'question': 'What is one measure that can be taken as a countermeasure for DNS enumeration?',
           'options': [
               'Enabling zone transfers to untrusted hosts',
               'Ensuring that private hostnames are referenced in public DNS records',
               'Disabling zone transfers to untrusted hosts',
               'Using free registration services for domains'
           ],
           'answer': 'Disabling zone transfers to untrusted hosts',
           'explanation': 'This prevents unauthorized access to DNS information.'
       }
    ]

    if 'score' not in st.session_state:
        st.session_state.score = 0

    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}:")
        st.write(q["question"])
        
        if isinstance(q["answer"], list):  # Check if the question allows multiple answers
            selected_options = st.multiselect(f"Select one or more options:", q["options"], key=f"q{i}")
        else:
            selected_option = st.radio(f"Select an option:", q["options"], key=f"q{i}", index=None)

        if st.button("Check Answer", key=f"btn{i}"):
            if isinstance(q["answer"], list):  # For multiple answers
                if set(selected_options) == set(q["answer"]):
                    st.session_state.score += 1
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answers are: {', '.join(q['answer'])}")
            else:  # For single answer
                if selected_option == q["answer"]:
                    st.session_state.score += 1
                    st.success("Correct!")
                elif selected_option is not None:
                    st.error(f"Incorrect. The correct answer is: {q['answer']}")
            
            if selected_option is not None or selected_options:
                with st.expander("Explanation"):
                    st.write(q["explanation"])
                
            st.write("---")  # adds a line after each question

    st.header("Quiz Results")
    st.write(f"Your final score is: {st.session_state.score}/{len(questions)}")

if __name__ == "__main__":
    main()