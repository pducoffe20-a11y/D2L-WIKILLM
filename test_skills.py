#!/usr/bin/env python3
"""
D2L Skills Testing Framework
Validates skills across different LLM providers
"""

import os
import json
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime

# Color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class TestStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    SKIP = "SKIP"
    WARNING = "WARNING"

@dataclass
class TestResult:
    test_id: str
    skill_name: str
    provider: str
    status: TestStatus
    message: str
    latency_ms: Optional[float] = None
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().isoformat()

class SkillTest:
    """Base class for skill tests"""

    def __init__(self, skill_name: str, test_id: str, provider: str = "claude-3-5-sonnet"):
        self.skill_name = skill_name
        self.test_id = test_id
        self.provider = provider

    def run(self) -> TestResult:
        raise NotImplementedError

class SkillsRegistry:
    """Registry of all D2L skills"""

    SKILLS = {
        'd2l-brain-search': {
            'category': 'Knowledge Search',
            'description': 'Search the private D2L Sales Brain',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku', 'gemini-pro'],
        },
        'd2l-sales-brief': {
            'category': 'Sales Enablement',
            'description': 'Generate evidence-first D2L briefs',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku', 'gemini-pro'],
        },
        'd2l-objection-coach': {
            'category': 'Sales Coaching',
            'description': 'Coach responses to buyer objections',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku', 'gemini-pro'],
        },
        'd2l-proof-finder': {
            'category': 'Evidence Discovery',
            'description': 'Locate D2L proof points and customer success evidence',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku'],
        },
        'd2l-brain-capture': {
            'category': 'Knowledge Management',
            'description': 'Capture new D2L sales intelligence',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku'],
        },
        'd2l-brain-curate': {
            'category': 'Knowledge Management',
            'description': 'Curate D2L sales brain entries',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku'],
        },
        'd2l-brain-refresh': {
            'category': 'Knowledge Management',
            'description': 'Refresh stale D2L brain entries',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku'],
        },
        'd2l-change-radar': {
            'category': 'Market Intelligence',
            'description': 'Monitor changes in D2L, customers, competitors',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku'],
        },
        'firecrawl': {
            'category': 'Web Crawling',
            'description': 'Crawl and extract data from web pages',
            'providers': ['claude-3-5-sonnet', 'claude-3-opus', 'claude-3-haiku', 'gemini-pro'],
        },
    }

    @classmethod
    def get_skill(cls, skill_name: str) -> Optional[Dict]:
        return cls.SKILLS.get(skill_name)

    @classmethod
    def list_skills(cls) -> List[str]:
        return list(cls.SKILLS.keys())

    @classmethod
    def list_by_category(cls, category: str) -> List[str]:
        return [skill for skill, info in cls.SKILLS.items() if info['category'] == category]

class SkillValidator:
    """Validates skill existence and configuration"""

    def __init__(self, skills_dir: Path):
        self.skills_dir = skills_dir

    def validate_skill_structure(self, skill_name: str) -> TestResult:
        """Check if skill has required files"""
        skill_path = self.skills_dir / skill_name / skill_name
        skill_md = skill_path / "SKILL.md"

        if skill_md.exists():
            return TestResult(
                test_id=f"structure_{skill_name}",
                skill_name=skill_name,
                provider="validation",
                status=TestStatus.PASS,
                message=f"Skill structure valid: {skill_md}"
            )
        else:
            return TestResult(
                test_id=f"structure_{skill_name}",
                skill_name=skill_name,
                provider="validation",
                status=TestStatus.FAIL,
                message=f"Missing SKILL.md at {skill_md}"
            )

    def validate_all_skills(self) -> List[TestResult]:
        """Validate all skills in the registry"""
        results = []
        for skill_name in SkillsRegistry.list_skills():
            result = self.validate_skill_structure(skill_name)
            results.append(result)
        return results

class TestSuite:
    """Runs a suite of tests"""

    def __init__(self):
        self.results: List[TestResult] = []

    def add_result(self, result: TestResult):
        self.results.append(result)

    def run_structure_validation(self, skills_dir: Path):
        """Validate all skills exist and have correct structure"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}=== Skill Structure Validation ==={Colors.RESET}")

        validator = SkillValidator(skills_dir)
        results = validator.validate_all_skills()

        for result in results:
            self.add_result(result)
            self._print_result(result)

    def run_registry_tests(self):
        """Test the skills registry"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}=== Skills Registry Tests ==={Colors.RESET}")

        # Test 1: Registry has all skills
        skills = SkillsRegistry.list_skills()
        if len(skills) >= 8:
            result = TestResult(
                test_id="registry_skills_count",
                skill_name="registry",
                provider="validation",
                status=TestStatus.PASS,
                message=f"Registry contains {len(skills)} skills"
            )
            self.add_result(result)
            self._print_result(result)
        else:
            result = TestResult(
                test_id="registry_skills_count",
                skill_name="registry",
                provider="validation",
                status=TestStatus.FAIL,
                message=f"Registry has only {len(skills)} skills, expected >= 8"
            )
            self.add_result(result)
            self._print_result(result)

        # Test 2: Category classification
        categories = set(info['category'] for info in SkillsRegistry.SKILLS.values())
        if len(categories) >= 5:
            result = TestResult(
                test_id="registry_categories",
                skill_name="registry",
                provider="validation",
                status=TestStatus.PASS,
                message=f"Skills organized in {len(categories)} categories: {', '.join(sorted(categories))}"
            )
            self.add_result(result)
            self._print_result(result)

        # Test 3: Provider support
        all_providers = set()
        for skill_info in SkillsRegistry.SKILLS.values():
            all_providers.update(skill_info['providers'])

        if 'claude-3-5-sonnet' in all_providers:
            result = TestResult(
                test_id="registry_providers",
                skill_name="registry",
                provider="validation",
                status=TestStatus.PASS,
                message=f"Multi-provider support: {', '.join(sorted(all_providers))}"
            )
            self.add_result(result)
            self._print_result(result)

    def run_workflow_tests(self):
        """Test workflow assignments"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}=== Workflow Assignment Tests ==={Colors.RESET}")

        # Test workflows have required skills
        workflows = {
            'Sales Research': ['d2l-brain-search', 'd2l-change-radar'],
            'Sales Coaching': ['d2l-objection-coach', 'd2l-brain-search'],
            'Knowledge Management': ['d2l-brain-capture', 'd2l-brain-curate', 'd2l-brain-refresh'],
            'Competitive Intelligence': ['d2l-change-radar', 'd2l-brain-search'],
            'Account Planning': ['d2l-sales-brief', 'd2l-brain-search'],
        }

        all_skills = SkillsRegistry.list_skills()

        for workflow_name, required_skills in workflows.items():
            missing = [s for s in required_skills if s not in all_skills]
            if not missing:
                result = TestResult(
                    test_id=f"workflow_{workflow_name.lower().replace(' ', '_')}",
                    skill_name=workflow_name,
                    provider="validation",
                    status=TestStatus.PASS,
                    message=f"Workflow '{workflow_name}' has all required skills"
                )
            else:
                result = TestResult(
                    test_id=f"workflow_{workflow_name.lower().replace(' ', '_')}",
                    skill_name=workflow_name,
                    provider="validation",
                    status=TestStatus.FAIL,
                    message=f"Workflow '{workflow_name}' missing skills: {missing}"
                )
            self.add_result(result)
            self._print_result(result)

    def _print_result(self, result: TestResult):
        """Print test result with color coding"""
        if result.status == TestStatus.PASS:
            status_str = f"{Colors.GREEN}✓ PASS{Colors.RESET}"
        elif result.status == TestStatus.FAIL:
            status_str = f"{Colors.RED}✗ FAIL{Colors.RESET}"
        elif result.status == TestStatus.WARNING:
            status_str = f"{Colors.YELLOW}⚠ WARN{Colors.RESET}"
        else:
            status_str = f"{Colors.YELLOW}⊘ SKIP{Colors.RESET}"

        latency_str = f" ({result.latency_ms:.0f}ms)" if result.latency_ms else ""
        print(f"  {status_str} | {result.test_id}: {result.message}{latency_str}")

    def print_summary(self):
        """Print test summary"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}=== Test Summary ==={Colors.RESET}")

        passed = sum(1 for r in self.results if r.status == TestStatus.PASS)
        failed = sum(1 for r in self.results if r.status == TestStatus.FAIL)
        warned = sum(1 for r in self.results if r.status == TestStatus.WARNING)
        skipped = sum(1 for r in self.results if r.status == TestStatus.SKIP)
        total = len(self.results)

        print(f"  Total:   {total}")
        print(f"  {Colors.GREEN}Passed:  {passed}{Colors.RESET}")
        if failed > 0:
            print(f"  {Colors.RED}Failed:  {failed}{Colors.RESET}")
        if warned > 0:
            print(f"  {Colors.YELLOW}Warned:  {warned}{Colors.RESET}")
        if skipped > 0:
            print(f"  Skipped: {skipped}")

        pass_rate = (passed / total * 100) if total > 0 else 0
        print(f"  Pass Rate: {pass_rate:.1f}%")

        return failed == 0

    def export_results(self, output_file: Path):
        """Export test results to JSON"""
        results_data = [asdict(r) for r in self.results]
        for r in results_data:
            r['status'] = r['status'].value if isinstance(r['status'], TestStatus) else r['status']

        with open(output_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'total_tests': len(self.results),
                'passed': sum(1 for r in self.results if r.status == TestStatus.PASS),
                'failed': sum(1 for r in self.results if r.status == TestStatus.FAIL),
                'results': results_data,
            }, f, indent=2)

        print(f"\nResults exported to {output_file}")

def main():
    """Main test execution"""
    print(f"{Colors.BOLD}D2L Skills Testing Framework{Colors.RESET}")
    print(f"Timestamp: {datetime.now().isoformat()}\n")

    # Determine skills directory
    repo_root = Path(__file__).parent
    skills_dir = repo_root / "unpacked" / "remote-vault" / "Remote Vault" / "skills"

    # Create test suite
    suite = TestSuite()

    # Run test categories
    if skills_dir.exists():
        suite.run_structure_validation(skills_dir)
    else:
        print(f"{Colors.YELLOW}Warning: Skills directory not found at {skills_dir}{Colors.RESET}")

    suite.run_registry_tests()
    suite.run_workflow_tests()

    # Print summary and export results
    success = suite.print_summary()

    # Export results
    output_file = repo_root / "test_results.json"
    suite.export_results(output_file)

    # Return exit code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
