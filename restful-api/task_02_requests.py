#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts(
    fetch_URL="https://jsonplaceholder.typicode.com/posts",
):
    resp = requests.get(fetch_URL)
    print(f"Status Code: {resp.status_code}")

    if resp.ok:
        dic_resp = resp.json()

        for dic in dic_resp:
            print(dic["title"])


def fetch_and_save_posts(
    fetch_URL="https://jsonplaceholder.typicode.com/posts",
):
    resp = requests.get(fetch_URL)
    print(f"Status Code: {resp.status_code}")

    if resp.status_code == 200:
        dic_resp = resp.json()
        fieldnames = ["id", "title", "body"]
        filename = "posts.csv"

        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f, fieldnames=fieldnames, extrasaction="ignore"
            )
            writer.writeheader()

            for dic in dic_resp:
                writer.writerow(dic)
