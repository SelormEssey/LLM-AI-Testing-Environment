import openai
import time

# Set up your OpenAI API key
openai.api_key = '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'

# Define the questions for benchmarking
questions = [
    "What is the capital of France?",
    "Who was the first president of the United States?",
    "What is the speed of light?",
    "What is the chemical symbol for water?",
    "What is the largest planet in our solar system?"
]

# Define the expected answers for comparison
expected_answers = {
    "What is the capital of France?": "Paris",
    "Who was the first president of the United States?": "George Washington",
    "What is the speed of light?": "299,792,458 meters per second",
    "What is the chemical symbol for water?": "H2O",
    "What is the largest planet in our solar system?": "Jupiter"
}

def get_model_response(question):
    """Send a question to the model and get the response"""
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # You can replace with other models if needed
        prompt=question,
        max_tokens=100,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def evaluate_answer(question, model_response):
    """Evaluate if the model's response matches the expected answer"""
    expected_answer = expected_answers.get(question, "")
    return model_response.lower() == expected_answer.lower()

def benchmark_model():
    """Benchmark the model with a set of questions"""
    total_time = 0
    correct_answers = 0
    total_questions = len(questions)

    for question in questions:
        start_time = time.time()
        model_response = get_model_response(question)
        end_time = time.time()

        elapsed_time = end_time - start_time
        total_time += elapsed_time

        if evaluate_answer(question, model_response):
            correct_answers += 1

        print(f"Question: {question}")
        print(f"Model's Response: {model_response}")
        print(f"Expected Answer: {expected_answers[question]}")
        print(f"Correct: {evaluate_answer(question, model_response)}")
        print(f"Response Time: {elapsed_time:.2f} seconds\n")

    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Total Time: {total_time:.2f} seconds")
    print(f"Accuracy: {correct_answers / total_questions * 100:.2f}%")

# Run the benchmark
benchmark_model()
