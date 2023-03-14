import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from "@angular/router";
import { UserProfileService } from "../user-profile.service";
import { UserProfile } from "../user-profile";
import { FormBuilder, FormControl, Validators } from "@angular/forms";

@Component({
  selector: 'app-edit-user-profile',
  templateUrl: './edit-user-profile.component.html',
  styleUrls: ['./edit-user-profile.component.css']
})
export class EditUserProfileComponent {
  editUserProfileForm;
  userProfile: UserProfile|null = null;

  constructor(private userProfileService: UserProfileService, private activatedRoute: ActivatedRoute, private router: Router, private formBuilder: FormBuilder) {
    this.editUserProfileForm = this.formBuilder.group({
      firstName: new FormControl(this.userProfile?.first_name),
      lastName: new FormControl(this.userProfile?.last_name),
      username: new FormControl(this.userProfile?.username),
      email: new FormControl(this.userProfile?.email, Validators.compose([Validators.pattern('^[A-Za-z0-9._%+-]+@iitb\.ac\.in$'), Validators.email])),
      dept: new FormControl(this.userProfile?.dept),
      mobileNumber: new FormControl(this.userProfile?.mobileNumber, Validators.compose([Validators.maxLength(10), Validators.minLength(10), Validators.pattern('[0-9]*')])), 
      degree: new FormControl(this.userProfile?.degree), 
      year: new FormControl(this.userProfile?.year, Validators.compose([Validators.min(1), Validators.max(4)])),
      alternateEmail: new FormControl(this.userProfile?.alternateEmail, Validators.email),
      subSystem: new FormControl(this.userProfile?.subSystem), 
      presentSystem: new FormControl(this.userProfile?.presentSystem), 
      Experience: new FormControl(this.userProfile?.Experience),
      topicWorkingOn: new FormControl(this.userProfile?.topicWorkingOn),
      profilePic: new FormControl(this.userProfile?.profilePic),
      hobbies: new FormControl(this.userProfile?.hobbies),
      softwaresKnown: new FormControl(this.userProfile?.softwaresKnown),
    });
  }

  ngOnInit(): void {
    const userId = this.activatedRoute.snapshot.paramMap.get('id');
    this.userProfileService.getUserProfile(userId).subscribe({
        next: (data) => {
          this.userProfile = data;
        },
        error: (error) => {
          console.log(error);
        }
      }
    );
  }

  onSubmit(): void {
    let firstName = this.editUserProfileForm.value.firstName;
    if (firstName === undefined || firstName === null || firstName === "") {
      if (this.userProfile === null) {
        console.log("firstName is null");
        return;
      }
      firstName = this.userProfile.first_name;
    }
    let lastName = this.editUserProfileForm.value.lastName;
    if (lastName === undefined || lastName === null || lastName === "") {
      if (this.userProfile === null) {
        console.log("lastName is null");
        return;
      }
      lastName = this.userProfile.last_name;
    }
    let username = this.editUserProfileForm.value.username;
    if (username === undefined || username === null || username === "") {
      if (this.userProfile === null) {
        console.log("username is null");
        return;
      }
      username = this.userProfile.username;
    }
    let email = this.editUserProfileForm.value.email;
    if (email === undefined || email === null || email === "") {
      if (this.userProfile === null) {
        console.log("email is null");
        return;
      }
      email = this.userProfile.email;
    }
    let dept = this.editUserProfileForm.value.dept;
    if (dept === undefined || dept === null || dept === "") {
      if (this.userProfile === null) {
        console.log("dept is null");
        return;
      }
      dept = this.userProfile.dept;
    }
    let mobileNumber = this.editUserProfileForm.value.mobileNumber;
    if (mobileNumber === undefined || mobileNumber === null || mobileNumber === "") {
      if (this.userProfile === null) {
        console.log("mobileNumber is null");
        return;
      }
      mobileNumber = this.userProfile.mobileNumber;
    }
    let degree = this.editUserProfileForm.value.degree;
    if (degree === undefined || degree === null || degree === "") {
      if (this.userProfile === null) {
        console.log("degree is null");
        return;
      }
      degree = this.userProfile.degree;
    }
    let year = this.editUserProfileForm.value.year;
    if (year === undefined || year === null || year === "") {
      if (this.userProfile === null) {
        console.log("year is null");
        return;
      }
      year = this.userProfile.year;
    }
    let alternateEmail = this.editUserProfileForm.value.alternateEmail;
    if (alternateEmail === undefined || alternateEmail === null || alternateEmail === "") {
      if (this.userProfile === null) {
        console.log("alternateEmail is null");
        return;
      }
      alternateEmail = this.userProfile.alternateEmail;
    }
    let subSystem = this.editUserProfileForm.value.subSystem;
    if (subSystem === undefined || subSystem === null || subSystem === "") {
      if (this.userProfile === null) {
        console.log("subSystem is null");
        return;
      }
      subSystem = this.userProfile.subSystem;
    }
    let presentSystem = this.editUserProfileForm.value.presentSystem;
    if (presentSystem === undefined || presentSystem === null || presentSystem === "") {
      if (this.userProfile === null) {
        console.log("presentSystem is null");
        return;
      }
      presentSystem = this.userProfile.presentSystem;
    }
    let Experience = this.editUserProfileForm.value.Experience;
    if (Experience === undefined || Experience === null || Experience === "") {
      if (this.userProfile === null) {
        console.log("Experience is null");
        return;
      }
      Experience = this.userProfile.Experience;
    }
    let topicWorkingOn = this.editUserProfileForm.value.topicWorkingOn;
    if (topicWorkingOn === undefined || topicWorkingOn === null || topicWorkingOn === "") {
      if (this.userProfile === null) {
        console.log("topicWorkingOn is null");
        return;
      }
      topicWorkingOn = this.userProfile.topicWorkingOn;
    }
    let profilePic = this.editUserProfileForm.value.profilePic;
    if (profilePic === undefined || profilePic === null || profilePic === "") {
      if (this.userProfile === null) {
        console.log("profilePic is null");
        return;
      }
      profilePic = this.userProfile.profilePic;
    }
    else {
      const reg = /^https:\/\/drive\.google\.com\/file\/d\/(.*?)\/.*?\?usp=.*$/g;
      profilePic = profilePic.replace(reg, "https://drive.google.com/uc?export=view&id=$1");
    }
    let hobbies = this.editUserProfileForm.value.hobbies;
    if (hobbies === undefined || hobbies === null || hobbies === "") {
      if (this.userProfile === null) {
        console.log("hobbies is null");
        return;
      }
      hobbies = this.userProfile.hobbies;
    }
    let softwaresKnown = this.editUserProfileForm.value.softwaresKnown;
    if (softwaresKnown === undefined || softwaresKnown === null || softwaresKnown === "") {
      if (this.userProfile === null) {
        console.log("softwaresKnown is null");
        return;
      }
      softwaresKnown = this.userProfile.softwaresKnown;
    }
    const id = this.userProfile?.id;
    if (id === undefined) {
      return;
    }
    const formData: UserProfile = {id, first_name: firstName, last_name: lastName, username, email, dept, mobileNumber, degree, year, alternateEmail, subSystem, presentSystem, Experience, topicWorkingOn, profilePic, hobbies, softwaresKnown};
    this.userProfileService.editUserProfile(formData).subscribe({
      next: (data) => {
        this.router.navigateByUrl(`/user-profile/${data.id}`);
      },
      error: (error) => {
        console.log(error);
      }
    });
  }

}
