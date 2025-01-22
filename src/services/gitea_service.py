import json
import requests
from typing import List, Dict, Any
from ..core.config import Config
from ..core.models import PRDetails
from gitea import Gitea

class GiteaService:
  def __init__(self, gitea_client: Gitea):
    """Initialize Gitea service with a client."""
    self.gitea_client = gitea_client

  def get_pr_details(self, event_path: str) -> PRDetails:
    """
    Extract pull request details from Gitea event data.
    
    Args:
      event_path: Path to Gitea event JSON file
    Returns:
      PRDetails object containing PR information
    """
    event_data = self._load_event_data(event_path)
    pull_number = self._extract_pull_number(event_data)
    repo_full_name = event_data["repository"]["full_name"]
    owner, repo = repo_full_name.split("/")
    
    repo_obj = self.gitea_client.get_repo(repo_full_name)
    pr = repo_obj.get_pull_request(pull_number)

    return PRDetails(owner, repo_obj.name, pull_number, pr.title, pr.body)

  def get_diff(self, owner: str, repo: str, pull_number: int) -> str:
    """
    Get the diff content for a pull request.
    
    Returns:
      Diff content as string or empty string if request fails
    """
    api_url = f"{Config.GITEA_URL}/api/v1/repos/{owner}/{repo}/pulls/{pull_number}.diff"
    headers = {
      'Authorization': f'token {Config.GITEA_TOKEN}',
      'Accept': 'application/vnd.gitea.v3.diff'
    }

    response = requests.get(api_url, headers=headers)
    return response.text if response.status_code == 200 else ""

  def create_review_comment(self, pr_details: PRDetails, comments: List[Dict[str, Any]]) -> None:
    """Create a review comment on the pull request."""
    repo = self.gitea_client.get_repo(f"{pr_details.owner}/{pr_details.repo}")
    pr = repo.get_pull_request(pr_details.pull_number)
    
    pr.create_review(
      body="AI generated review comments",
      comments=comments,
      review_state="COMMENT"
    )

  def _load_event_data(self, event_path: str) -> Dict:
    """Load Gitea event data from JSON file."""
    with open(event_path, "r") as f:
      return json.load(f)

  def _extract_pull_number(self, event_data: Dict) -> int:
    """Extract pull request number from event data."""
    if "issue" in event_data and "pull_request" in event_data["issue"]:
      return event_data["issue"]["number"]
    return event_data["number"]
