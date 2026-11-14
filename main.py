from agent.graph import build_graph

def main():
    app = build_graph()
    print("NEWs Agent Graph is ready to run")

    while True:
        question= input("\n Your question:")
        if question.lower() in ["exit","quit"]:
            print("Exiting the agent. Goodbye!")
            break
        if not question.strip():
            print("Please enter a valid question.")
            continue

        result =app.invoke({"question":question})
        print("\nAnswer:", result["answer"])
        print("Steps taken:", " -> ".join(result.get("steps", [])))


if __name__ == "__main__":
    main()
