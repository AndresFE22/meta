def calculate_learning_style_score(self, selected_styles):
        selected_styles = {
             1: {'style': 'Activo/Reflexivo', 'response': 'a'}, 2: {'style': 'Sensorial/Intuitivo', 'response': 'a'}, 3: {'style': 'Visual/Verbal', 'response': 'a'}, 4: {'style': 'Secuencial/Global', 'response': 'a'}, 5: {'style': 'Activo/Reflexivo', 'response': 'a'}, 6: {'style': 'Sensorial/Intuitivo', 'response': 'a'}, 7: {'style': 'Visual/Verbal', 'response': 'a'}, 8: {'style': 'Secuencial/Global', 'response': 'a'}, 9: {'style': 'Activo/Reflexivo', 'response': 'a'}, 10: {'style': 'Sensorial/Intuitivo', 'response': 'a'}, 11: {'style': 'Visual/Verbal', 'response': 'a'}, 12: {'style': 'Secuencial/Global', 'response': 'a'}, 13: {'style': 'Activo/Reflexivo', 'response': 'a'}, 14: {'style': 'Sensorial/Intuitivo', 'response': 'a'}, 15: {'style': 'Visual/Verbal', 'response': 'a'}, 16: {'style': 'Secuencial/Global', 'response': 'a'}, 17: {'style': 'Activo/Reflexivo', 'response': 'a'}, 18: {'style': 'Sensorial/Intuitivo', 'response': 'a'}, 19: {'style': 'Visual/Verbal', 'response': 'a'}, 20: {'style': 'Secuencial/Global', 'response': 'a'}
        }
        results = []

        styles_data = {
                'style_1': {
                    'Activo': 0,
                    'Reflexivo': 0
                },
                'style_2': {
                    'Sensorial': 0,
                    'Intuitivo': 0
                },
                'style_3': {
                    'Visual': 0,
                    'Verbal': 0
                },
                'style_4': {
                    'Secuencial': 0,
                    'Global': 0
                },
        }
        for question, data in selected_styles.items():
            style, response = data['style'], data['response']
            first_style, second_style = style.split('/')
            if response == 'a':
                styles_data[first_style] += 1
            elif response == 'b':
                styles_data[second_style] += 1
            max_score = max(styles_data.values())
            min_score = min(styles_data.values())
            subtraction = max_score - min_score
            dominant_style = [styles for styles, score in styles_data.items() if score == max_score]
            results.append({'dominant_style': dominant_style, 'subtraction': subtraction})

            return results