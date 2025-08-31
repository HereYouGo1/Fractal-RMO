#!/usr/bin/env python3
"""
Session End Validator - MANDATORY Before Ending Any Work Session
Ensures all documentation is updated according to contribution guidelines.
Version: 1.0
Created: 2025-08-31
"""

import os
import sys
import datetime
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Color codes for terminal output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

class SessionValidator:
    def __init__(self):
        self.base_path = Path("/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)")
        self.tracking_path = self.base_path / "12--(Progress)_(Tracking)_(What)_(We)_(Did)"
        self.errors = []
        self.warnings = []
        self.success = []
        
    def check_project_overview(self) -> bool:
        """Check if Project Overview was updated recently."""
        overview_file = self.tracking_path / "0.2--(Project)_(Overview)_(Current)_(State)" / "(Project)_(Overview)_(Current)_(State).md"
        
        if not overview_file.exists():
            self.errors.append("Project Overview file not found!")
            return False
            
        # Check last modified time
        mtime = datetime.datetime.fromtimestamp(overview_file.stat().st_mtime)
        now = datetime.datetime.now()
        hours_ago = (now - mtime).total_seconds() / 3600
        
        if hours_ago > 2:
            self.errors.append(f"Project Overview last updated {hours_ago:.1f} hours ago (>2 hours)")
            self.errors.append("  FIX: Update short-term memory using template in §2.1")
            return False
        else:
            self.success.append(f"Project Overview updated {hours_ago:.1f} hours ago ✓")
            
        # Check for required sections
        with open(overview_file, 'r') as f:
            content = f.read()
            
        required_sections = [
            "SHORT-TERM MEMORY",
            "CURRENT WORK CONTEXT",
            "TECHNICAL SETUP"
        ]
        
        for section in required_sections:
            if section not in content:
                self.errors.append(f"Missing section: {section}")
                return False
                
        return True
        
    def check_work_files(self) -> bool:
        """Check if work files have recent entries."""
        work_files = list(self.tracking_path.glob("[0-9]*--*/*.md"))
        
        if not work_files:
            self.warnings.append("No work files found yet (OK if just starting)")
            return True
            
        # Find most recent work file
        latest_file = max(work_files, key=lambda f: f.stat().st_mtime)
        mtime = datetime.datetime.fromtimestamp(latest_file.stat().st_mtime)
        now = datetime.datetime.now()
        hours_ago = (now - mtime).total_seconds() / 3600
        
        if hours_ago > 4:
            self.errors.append(f"Latest work file updated {hours_ago:.1f} hours ago (>4 hours)")
            self.errors.append(f"  File: {latest_file.name}")
            self.errors.append("  FIX: Add work entry using template in §3.2")
            return False
        else:
            self.success.append(f"Work file updated {hours_ago:.1f} hours ago ✓")
            
        return True
        
    def check_readmes(self) -> bool:
        """Check if README files exist where needed."""
        issues = []
        
        for folder in self.base_path.rglob("*/"):
            # Skip hidden folders and venv
            if any(part.startswith('.') for part in folder.parts):
                continue
            if 'venv' in folder.parts or '__pycache__' in folder.parts:
                continue
                
            # Count items in folder
            items = list(folder.iterdir())
            visible_items = [i for i in items if not i.name.startswith('.')]
            
            if len(visible_items) >= 2:
                readme_folder = folder / "0--(README_Folder)"
                readme_file = readme_folder / "(README_Folder).md"
                
                if not readme_file.exists():
                    relative_path = folder.relative_to(self.base_path)
                    issues.append(str(relative_path))
                    
        if issues:
            self.errors.append(f"Folders missing README ({len(issues)} found):")
            for folder in issues[:5]:  # Show first 5
                self.errors.append(f"  - {folder}")
            if len(issues) > 5:
                self.errors.append(f"  ... and {len(issues)-5} more")
            self.errors.append("  FIX: Create 0--(README_Folder) using template in §5.3")
            return False
        else:
            self.success.append("All folders have required READMEs ✓")
            
        return True
        
    def check_timestamps(self) -> bool:
        """Check if recent entries use correct timestamp format."""
        # This would parse recent files and validate timestamp formats
        # For now, just a reminder
        self.warnings.append("REMINDER: Use format [YYYY-MM-DD | HH:MM-HH:MM PST | Agent-Version]")
        return True
        
    def run_validation(self) -> bool:
        """Run all validation checks."""
        print(f"\n{BOLD}{'='*60}{RESET}")
        print(f"{BOLD}SESSION END VALIDATOR v1.0{RESET}")
        print(f"{BOLD}{'='*60}{RESET}\n")
        
        all_passed = True
        
        # Run checks
        checks = [
            ("Project Overview", self.check_project_overview),
            ("Work Files", self.check_work_files),
            ("README Files", self.check_readmes),
            ("Timestamp Format", self.check_timestamps)
        ]
        
        for name, check_func in checks:
            print(f"Checking {name}...", end=" ")
            if check_func():
                print(f"{GREEN}✓{RESET}")
            else:
                print(f"{RED}✗{RESET}")
                all_passed = False
                
        print(f"\n{BOLD}{'='*60}{RESET}")
        
        # Show results
        if self.success:
            print(f"\n{GREEN}{BOLD}✅ PASSED CHECKS:{RESET}")
            for msg in self.success:
                print(f"  {msg}")
                
        if self.warnings:
            print(f"\n{YELLOW}{BOLD}⚠️  WARNINGS:{RESET}")
            for msg in self.warnings:
                print(f"  {msg}")
                
        if self.errors:
            print(f"\n{RED}{BOLD}❌ VALIDATION FAILED:{RESET}")
            print(f"{RED}MISSING UPDATES:{RESET}")
            for msg in self.errors:
                print(f"  {msg}")
                
        print(f"\n{BOLD}{'='*60}{RESET}")
        
        if all_passed:
            print(f"{GREEN}{BOLD}✅ VALIDATION PASSED{RESET}")
            print("Session Complete: OK to end")
        else:
            print(f"{RED}{BOLD}❌ VALIDATION FAILED{RESET}")
            print("Fix issues above before ending session")
            print(f"\nRefer to: {BLUE}0.1--(Contribution)_(Guidelines)_(MUST_READ){RESET}")
            
        print(f"{BOLD}{'='*60}{RESET}\n")
        
        return all_passed

def main():
    validator = SessionValidator()
    passed = validator.run_validation()
    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()
