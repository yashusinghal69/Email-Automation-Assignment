import pandas as pd
import json
 

def categorize_job_title(job_title):
    """Categorize job title into predefined categories"""
    if pd.isna(job_title) or str(job_title).lower() in ['','nan']:
        return 'other'
    
    job_title_lower = str(job_title).lower()
    
    # Define job categories with keywords
    job_categories = {
        'student': ['student', 'undergraduate', 'intern', 'fresher', 'college', 'university'],
        'developer': ['developer', 'engineer', 'programmer', 'sde', 'software', 'full stack', 'backend', 'frontend', 'web dev', 'dev'],
        'product': ['product manager', 'pm', 'product', 'associate product', 'senior product', 'director product', 'lead product'],
        'data': ['data scientist', 'data analyst', 'data engineer', 'ml engineer', 'ai engineer', 'machine learning', 'data science'],
        'executive': ['ceo', 'cto', 'coo', 'founder', 'director', 'head', 'vp', 'vice president', 'chief'],
        'consultant': ['consultant', 'analyst', 'advisor', 'specialist'],
        'other': ['freelancer', 'unemployed', 'teacher', 'professor', 'manager']
    }
    
    for category, keywords in job_categories.items():
        for keyword in keywords:
            if keyword in job_title_lower:
                return category
    
    return 'other'

def create_email_message(first_name, job_title, job_category, has_joined, has_linkedin):
    """Generate professional email message"""
    
    if has_joined:
        # Messages for event participants
        if job_category == 'student':
            return f"Dear {first_name},\n\nThank you for attending our AI workshop! As a student, you're perfectly positioned to leverage cutting-edge AI tools in your studies and future career. We'd like to offer you exclusive access to our student AI toolkit.\n\nBest regards,\nThe AI Workshop Team"
        
        elif job_category == 'developer':
            return f"Hi {first_name},\n\nGreat to have you at our AI session! Given your background as a {job_title}, you'll find our new AI development suite particularly valuable for streamlining your coding workflow and boosting productivity.\n\nLet's schedule a demo at your convenience.\n\nBest,\nThe AI Workshop Team"
        
        elif job_category == 'product':
            return f"Hello {first_name},\n\nThank you for joining our AI workshop! As a {job_title}, you understand the importance of data-driven decisions. Our AI analytics platform can transform how you approach product strategy and user insights.\n\nWould you be interested in exploring a pilot program?\n\nRegards,\nThe AI Workshop Team"
        
        elif job_category == 'data':
            return f"Dear {first_name},\n\nIt was wonderful having you at our AI workshop! Your expertise as a {job_title} aligns perfectly with our advanced AI platform. We believe our tools can significantly enhance your data processing and model development capabilities.\n\nLet's discuss how we can support your work.\n\nBest regards,\nThe AI Workshop Team"
        
        elif job_category == 'executive':
            return f"Dear {first_name},\n\nThank you for attending our AI workshop! As a {job_title}, you recognize AI's transformative potential for business growth. We'd welcome the opportunity to discuss how our enterprise AI solutions can drive innovation in your organization.\n\nBest regards,\nThe AI Workshop Team"
        
        else:
            return f"Dear {first_name},\n\nThank you for participating in our AI workshop! We believe AI can enhance productivity across all industries, and we'd love to show you how our solutions can benefit your specific role.\n\nLooking forward to continuing the conversation.\n\nBest regards,\nThe AI Workshop Team"
    
    else:
        # Messages for non-participants
        if job_category == 'student':
            return f"Hi {first_name},\n\nWe missed you at our recent AI workshop! Understanding that student schedules can be challenging, we're organizing a special session focused on AI tools for academic success and career preparation.\n\nWould this timing work better for you?\n\nBest regards,\nThe AI Workshop Team"
        
        elif job_category == 'developer':
            return f"Hello {first_name},\n\nWe hope you're doing well! We noticed you couldn't make it to our last AI workshop. We're planning a technical deep-dive session specifically for developers like yourself, focusing on AI coding assistants and development automation.\n\nInterested in joining?\n\nBest,\nThe AI Workshop Team"
        
        elif job_category == 'product':
            return f"Hi {first_name},\n\nWe missed you at our recent AI workshop! Knowing how valuable your time is as a {job_title}, we're organizing a focused session on AI applications in product management and strategy.\n\nWould this be of interest?\n\nRegards,\nThe AI Workshop Team"
        
        elif job_category == 'data':
            return f"Dear {first_name},\n\nWe hope this message finds you well! We missed you at our recent AI workshop. We're planning an advanced session tailored for data professionals, covering cutting-edge AI/ML techniques and tools.\n\nWould you like to join us?\n\nBest regards,\nThe AI Workshop Team"
        
        elif job_category == 'executive':
            return f"Dear {first_name},\n\nWe understand your busy schedule prevented you from attending our recent AI workshop. We're organizing an executive briefing on AI's strategic impact on business transformation and competitive advantage.\n\nWould this format work better for you?\n\nBest regards,\nThe AI Workshop Team"
        
        else:
            return f"Hi {first_name},\n\nWe missed you at our recent AI workshop! We're organizing another session with flexible timing and broader AI applications that might better suit your schedule and interests.\n\nHope to see you next time!\n\nBest regards,\nThe AI Workshop Team"

def create_linkedin_message(first_name, job_title, job_category, has_joined, has_linkedin):
    """Generate professional LinkedIn message"""
    
    if not has_linkedin:
        return "Unable to send LinkedIn message - Profile not available"
    
    if has_joined:
        # LinkedIn messages for event participants
        if job_category == 'student':
            return f"Hi {first_name}! Thanks for joining our AI workshop. As a student, you're at the perfect stage to integrate AI into your learning journey. I'd love to connect and share some exclusive AI resources for students. Looking forward to connecting!"
        
        elif job_category == 'developer':
            return f"Hi {first_name}! Great meeting you at our AI workshop. Your background as a {job_title} caught my attention - I think you'd be really interested in our new AI development tools. Would love to connect and continue our conversation about AI in software development."
        
        elif job_category == 'product':
            return f"Hello {first_name}! Thank you for attending our AI workshop. As a {job_title}, I'm sure you see the immense potential of AI in product development. I'd like to connect and discuss how AI can transform product strategy. Let's stay in touch!"
        
        elif job_category == 'data':
            return f"Hi {first_name}! It was great having you at our AI workshop. Your expertise as a {job_title} would be valuable for our community. I'd love to connect and explore potential collaboration opportunities in the AI space."
        
        elif job_category == 'executive':
            return f"Dear {first_name}, Thank you for attending our AI workshop. Your perspective as a {job_title} on AI's business impact was insightful. I'd welcome the opportunity to connect and discuss AI strategy further. Looking forward to your connection!"
        
        else:
            return f"Hi {first_name}! Thanks for joining our AI workshop. It was great meeting professionals from diverse backgrounds. I'd love to connect and keep you updated on how AI can enhance your work. Looking forward to connecting!"
    
    else:
        # LinkedIn messages for non-participants
        if job_category == 'student':
            return f"Hi {first_name}! I noticed you registered for our AI workshop but couldn't make it. No worries! As a student, I think you'd find great value in our upcoming sessions. I'd love to connect and keep you informed about future opportunities."
        
        elif job_category == 'developer':
            return f"Hello {first_name}! We missed you at our recent AI workshop. Given your role as a {job_title}, I think our upcoming technical sessions would be right up your alley. Would love to connect and share details about developer-focused AI events."
        
        elif job_category == 'product':
            return f"Hi {first_name}! We missed you at our AI workshop, but I understand how busy product roles can be. I'd love to connect and share insights about AI applications in product management that might interest you."
        
        elif job_category == 'data':
            return f"Hello {first_name}! We missed you at our recent AI workshop. As a {job_title}, I think you'd appreciate our advanced AI sessions. I'd like to connect and keep you informed about future data-focused events."
        
        elif job_category == 'executive':
            return f"Dear {first_name}, We understand you couldn't attend our recent AI workshop. As a {job_title}, your insights on AI's strategic implications would be valuable. I'd like to connect and discuss executive-level AI initiatives."
        
        else:
            return f"Hi {first_name}! We missed you at our recent AI workshop. I'd love to connect and keep you updated on future sessions that might align better with your schedule and interests."


def generate_all_messages(df):
    """Generate personalized messages for all users"""
    messages = []
    
    for index, row in df.iterrows():
        # Extract user information
        first_name = row.get('first_name', 'there')
        if pd.isna(first_name):
            first_name = 'there'
        
        job_title = row.get('Job Title', 'Professional')
        if pd.isna(job_title):
            job_title = 'Professional'
        
        email = row.get('email', '')
        has_joined = row.get('has_joined_event', False)
        missing_linkedin = row.get('missing_linkedin', True)
        
        # Convert string boolean to actual boolean
        if isinstance(has_joined, str):
            has_joined = has_joined.lower() == 'true'
        if isinstance(missing_linkedin, str):
            missing_linkedin = missing_linkedin.lower() == 'true'
        
        # Categorize job title
        job_category = categorize_job_title(job_title)
        has_linkedin = not missing_linkedin
        
        # Generate messages
        email_message = create_email_message(first_name, job_title, job_category, has_joined, has_linkedin)
        linkedin_message = create_linkedin_message(first_name, job_title, job_category, has_joined, has_linkedin)
        
        # Store message data
        message_data = {
            'email': email,
            'email_message': email_message,
            'linkedin_message': linkedin_message,
            'first_name': first_name,
            'job_title': job_title,
            'job_category': job_category,
            'has_joined_event': has_joined,
            'has_linkedin': has_linkedin
        }
        
        messages.append(message_data)
    
    print(f"✅ Generated {len(messages)} personalized messages")
    return messages


def save_csv_output(messages, output_path='personalized_messages.csv'):
    output_data = []
    
    for msg in messages:
        output_data.append({
            'email': msg['email'],
            'email_message': msg['email_message'],
            'linkedin_message': msg['linkedin_message']
        })
    
    output_df = pd.DataFrame(output_data)
    output_df.to_csv(output_path, index=False)
    print(f"✅ CSV output saved to {output_path}")


def save_json_output(messages, output_path='personalized_messages.json'):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)
    print(f"✅ JSON output saved to {output_path}")

        
def display_statistics(messages):
    """Display statistics about the messaging"""
    total = len(messages)
    joined = sum(1 for msg in messages if msg['has_joined_event'])
    missed = total - joined
    has_linkedin = sum(1 for msg in messages if msg['has_linkedin'])
    missing_linkedin = total - has_linkedin
    
    # Count by categories
    categories = {}
    for msg in messages:
        cat = msg['job_category']
        categories[cat] = categories.get(cat, 0) + 1
    
    print(f"\n{'='*60}")
    print(f"📊 MESSAGING STATISTICS")
    print(f"{'='*60}")
    print(f"📧 Total Messages Generated: {total}")
    print(f"✅ Event Participants: {joined}")
    print(f"❌ Event Non-Participants: {missed}")
    print(f"🔗 Users with LinkedIn: {has_linkedin}")
    print(f"❌ Users without LinkedIn: {missing_linkedin}")
    print(f"\n📋 Job Category Distribution:")
    for category, count in sorted(categories.items()):
        print(f"   {category.title()}: {count}")
    print(f"{'='*60}")




def main():
    
    # Load data
    csv_file = 'cleaned_output.csv'
    df = pd.read_csv(csv_file)
    print(f"✅ Successfully loaded {len(df)} records from CSV")

    # Generate messages
    messages = generate_all_messages(df)
    
    # Save outputs
    save_csv_output(messages, 'personalized_messages.csv')
    save_json_output(messages, 'personalized_messages.json')
    
    # Display statistics
    display_statistics(messages)
    
    print(f"\n✅ All outputs saved successfully!")
    
if __name__ == "__main__":
    main()
