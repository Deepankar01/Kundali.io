def validate_shadbala(threshold=6000):
    def decorator(fn):
        def wrapper(chart, shadbala_data, *args, **kwargs):
            result = fn(chart, *args, **kwargs)
            if result is None:
                return None
            if isinstance(result, list):
                for r in result:
                    r["shadbala_status"] = {
                        planet: shadbala_data.get(planet, 0) for planet in r["planets"]
                    }
                    r["valid"] = all(
                        shadbala_data.get(planet, 0) >= threshold for planet in r["planets"]
                    )
                return result
            result["shadbala_status"] = {
                planet: shadbala_data.get(planet, 0) for planet in result["planets"]
            }
            result["valid"] = all(
                shadbala_data.get(planet, 0) >= threshold for planet in result["planets"]
            )
            return result
        return wrapper
    return decorator
