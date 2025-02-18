from django.shortcuts import render

def cv_view(request):
    cv_data = {
        'name': 'Shweta Shekhar',
        'title': 'Senior Software Engineer at GEP Worldwide | Machine Learning Enthusiast',
        'summary': "Experienced in software engineering, machine learning, and artificial intelligence. Passionate about ML and AI-driven insights.",
        'skills': [
            'C#', 'AngularJS', 'Angular 5', '.NET Core', 'Python', 'SQL', 'Streamlit', 'Machine Learning', 
            'RESTful Services', 'Information Visualization', 'Azure', 'ADO.NET', 'LINQ', 'WCF', 'jQuery', 
            'AJAX', 'Elasticsearch', 'Kibana', 'Azure CI/CD'
        ],
        'experience': [
            {
                'position': 'Senior Software Engineer | Software Engineer | Associate Software Engineer',
                'company': 'GEP Worldwide',
                'years': 'Aug 2020 - Sep 2024',
                'details': [
                    "Guided juniors in developing and deploying scalable solutions for GEP SMART, a cloud-based sourcing and procurement platform on Microsoft Azure, achieving a 10% increase in processing efficiency and a 10% reduction in operational costs.",
                    "Leveraged Git, GitHub, and Azure CI/CD pipelines for version control and deployment, improving productivity by 20-25% and reducing post-release bugs.",
                    "Developed APIs using RESTful/MVC, WCF, and Web API, boosting application response time by 30% and integrating with third-party E-Sign providers.",
                    "Managed Microsoft SQL databases, reducing query execution time by 20%.",
                    "Enhanced real-time data search by 10% and operational efficiency by 5% using Elasticsearch and Kibana.",
                    "Awarded Kudos Certificate for delivering client-critical enhancements, reducing feature release time by 25% and fostering a 20% increase in engineer satisfaction."
                ]
            },
            {
                'position': 'Machine Learning Intern',
                'company': 'Bhabha Atomic Research Center (BARC) - SuperComputing Division',
                'years': 'May 2019 - Jun 2019',
                'details': [
                    "Designed machine learning models for network anomaly detection using Python, R, and Elasticsearch, enhancing detection accuracy by 15%.",
                    "Optimized algorithms using Isolation Forest, SVM, and K-Means Clustering, reducing false positives by 20%."
                ]
            },
            {
                'position': 'Machine Learning Intern',
                'company': 'Study League IT Solutions Pvt Ltd',
                'years': 'May 2019 - Jun 2019',
                'details': [
                    "Created an automated broadcasting system for sending messages, images, documents, and stickers via Web WhatsApp messaging system.",
                    "Automated broadcasting using Python and Selenium WebDriver, reducing manual broadcast time by 50%."
                ]
            }
        ],
        'education': [
            {
                'degree': "Master of Science in Computer Science",
                'institution': "New York University, Brooklyn, NY",
                'years': "Sep 2024 - May 2026",
                'gpa': "GPA 4.0/4.0",
                'coursework': [
                    "Foundations of Data Science (A)", 
                    "Machine Learning (A)", 
                    "Information Visualization (A)"
                ]
            },
            {
                'degree': "Bachelor of Engineering in Computer Engineering",
                'institution': "University of Mumbai, SIES",
                'years': "Aug 2016 - Oct 2020",
                'awards': "Silver Medalist (2nd Rank) with 9.36/10 CGPA in Computer Engineering Department"
            }
        ],
        'projects': [
            {
                'title': "Causal Impact of Weather on Food Delivery",
                'timeline': "Sep 2024 - Nov 2024",
                'details': "Investigated the impact of weather conditions and traffic density on delivery times using PyMC, Pandas, and DAGs, optimizing logistics efficiency.",
                'link': "https://github.com/shwetashekhar98/Foundation-of-Data-Science-Project"
            },
            {
                'title': "Advanced Information Visualization for Stock Market Analysis",
                'timeline': "Sep 2024 - Nov 2024",
                'details': "Implemented an advanced stock market visualization tool using Streamlit, Dash, D3.js, and Matplotlib to analyze NYSE performance, generate actionable insights, perform risk-return analysis, and deliver sentiment-based recommendations.",
                'link': "https://github.com/shwetashekhar98/InfoVizProject"
            },
            {
                'title': "Comparison of 3 Reinforcement Learning Algorithms for Solving 2048",
                'timeline': "Sep 2024 - Nov 2024",
                'details': "Evaluated Q-learning, DQN, and MCTS algorithms for solving the 2048 game using Python, TensorFlow, and NumPy, demonstrating DQN's consistent success, algorithmic efficiency, and scalability in high-dimensional, stochastic environments.",
                'link': "https://github.com/shwetashekhar98/Machine-Learning-Final-Project"
            },
            {
                'title': "ML Based E-Learning System for Learning Disability Detection",
                'timeline': "Jun 2018 – May 2020",
                'details': "Coauthored and presented a research paper at IEEE ICCCA on a Moodle-based LMS using PCA, Random Forest, and SVM, achieving 90% accuracy in detecting learning disabilities.",
                'link': "https://github.com/shwetashekhar98/E-Learning-System-for-Detection-of-Learning-Disability"
            }
        ],
        'contact': {
            'email': "ss19623@nyu.edu",
            'phone': "(917)-648-3036",
            'linkedin': "linkedin.com/in/shwetashekhar98",
            'github': "github.com/shwetashekhar98"
        }
    }
    return render(request, 'cv.html', cv_data)
