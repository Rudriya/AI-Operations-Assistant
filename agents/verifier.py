def verifier_agent(executor_results: list) -> dict:
    successful_results = []
    errors = []

    for item in executor_results:
        if "result" in item:
            successful_results.append(item)
        else:
            errors.append(item)

    if successful_results and not errors:
        status = "success"
    elif successful_results and errors:
        status = "partial_success"
    else:
        status = "failed"

    return {
        "status": status,
        "results": successful_results,
        "errors": errors
    }