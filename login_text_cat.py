def elements_category(elements_extracted):
    removed_words = ["trending_up", "trending_down", "description", "domain"]
    
    elements_extracted = [word for word in elements_extracted if word not in removed_words]

    #Process the elements
    for rate in elements_extracted:
        try:
            if "15 Day" in rate:
                print(elements_extracted)
                daily_15_rate = elements_extracted[elements_extracted.index(rate)+1]
                daily_15_minmax = elements_extracted[elements_extracted.index(rate)+2]
                daily_15_domain = elements_extracted[elements_extracted.index(rate)+3]
                daily_15_company = elements_extracted[elements_extracted.index(rate)+4]
                # print("rate 15: " + daily_15_rate)
                # print("minmax 15: " + daily_15_minmax)
                # print("report company 15: " + daily_15_company)
                # print("report domain 15: " + daily_15_domain)

            if "3 Day" in rate:
                print(elements_extracted)
                daily_3_rate = elements_extracted[elements_extracted.index(rate)+1]
                daily_3_minmax = elements_extracted[elements_extracted.index(rate)+2]
                daily_3_domain = elements_extracted[elements_extracted.index(rate)+3]
                daily_3_company = elements_extracted[elements_extracted.index(rate)+4]
                # print("rate 3: " + daily_3_rate)
                # print("minmax 3: " + daily_3_minmax)
                # print("report company 3: " + daily_3_company)
                # print("report domain 3: " + daily_3_domain)

            if "30 Day" in rate:
                print(elements_extracted)
                daily_30_rate = elements_extracted[elements_extracted.index(rate)+1]
                daily_30_minmax = elements_extracted[elements_extracted.index(rate)+2]
                daily_30_domain = elements_extracted[elements_extracted.index(rate)+3]
                daily_30_company = elements_extracted[elements_extracted.index(rate)+4]
                # print("rate 30: " + daily_30_rate)
                # print("minmax 30: " + daily_30_minmax)
                # print("report company 30: " + daily_30_company)
                # print("report domain 30: " + daily_30_domain)

            if "7 Day" in rate:
                print(elements_extracted)
                daily_7_rate = elements_extracted[elements_extracted.index(rate)+1]
                daily_7_minmax = elements_extracted[elements_extracted.index(rate)+2]
                daily_7_domain = elements_extracted[elements_extracted.index(rate)+3]
                daily_7_company = elements_extracted[elements_extracted.index(rate)+4]
                # print("rate 7: " + daily_7_rate)
                # print("minmax 7: " + daily_7_minmax)
                # print("report company 7: " + daily_7_company)
                # print("report domain 7: " + daily_7_domain)

        except Exception as e:
            print(f"Error processing rate {rate}: {e}")
            continue  # Continue to the next iteration if there is an error
 