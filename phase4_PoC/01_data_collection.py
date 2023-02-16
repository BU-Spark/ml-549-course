import os
import json
import pandas as pd
import logging
from github import Github
from dotenv import find_dotenv, load_dotenv
from github_handling import connect_to_source, GITHUB_TIMEOUT_SECONDS, GitHubSingleton, GithubHandler

import process_pr
# import ceph_comm

load_dotenv(find_dotenv(), override=True)

_LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# get the org/repo from env vars
ORG = os.getenv("GITHUB_ORG")
REPO = os.getenv("GITHUB_REPO")
TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
RAW_DATA_PATH = os.path.join(ORG, REPO)

gs = GitHubSingleton()
print("GitHub Singleton: ", gs.github)

gh = GithubHandler(gs.github)
print("GitHub Handler: ", gh)

# This uses 1 API call
repo = connect_to_source(ORG+'/'+REPO, gh)

# This typically uses 9 API calls
prs = repo.get_pulls(state='closed')
pr_ids = [pr.number for pr in prs]
len_pr_ids = len(pr_ids)
_LOGGER.info(f"There are {len_pr_ids} closed PR's in {ORG}/{REPO}")

closed_prs_df = pd.DataFrame(pr_ids, columns=["closed_pr_ids"])
CLOSED_PR_IDS_FILENAME = os.path.join("phase4_PoC/CLOSED_PR_IDS.parquet")
closed_prs_df.to_parquet(CLOSED_PR_IDS_FILENAME)  # where to save it, usually as a .pkl

for idx, pr in enumerate(prs):
    _LOGGER.info(f"{idx+1}/{len_pr_ids}...PR's remaining")    
    d = process_pr.parse_pr_with_mi(pr,gh)
    pr_df = pd.DataFrame.from_dict(d, orient="index")
    pr_df = pr_df.transpose()

    PR_FILENAME = os.path.join("phase4_PoC/PRs/"+ str(pr.number) + ".json")
    print("collected PR", RAW_DATA_PATH+"/"+PR_FILENAME)

    pr_df.to_json(PR_FILENAME)
