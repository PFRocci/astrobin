import { Injectable } from '@angular/core';
import { UserProfileModel } from "../models/common/userprofile.model";

@Injectable({
  providedIn: 'root'
})
export class LegacyRoutesService {
  HOME = "/";
  LOGIN = "/accounts/login/";
  REGISTER = "/accounts/register/";
  SUBSCRIPTIONS = "/subscriptions/";
  UPLOAD = "/upload/";
  COMMERCIAL_PRODUCTS = (profile: UserProfileModel) => `/users/${profile.userObject.username}/commercial/products/`;
  GALLERY = (profile: UserProfileModel) => `/users/${profile.userObject.username}/`;
  BOOKMARKS = (profile: UserProfileModel) => `/users/${profile.userObject.username}/bookmarks/`;
  PLOTS = (profile: UserProfileModel) => `/users/${profile.userObject.username}/plots/`;
  RAWDATA = "/rawdata/";
  RAWDATA_PRIVATE_SHARED_FOLDERS = "/rawdata/privatesharedfolders/";
  RAWDATA_PUBLIC_DATA_POOLS  = "/rawdata/publicdatapools/";
  RAWDATA_HELP = "/rawdata/help/1/";
  INBOX = "/messages/inbox/";
  API_KEYS = (profile: UserProfileModel) => `/users/${profile.userObject.username}/apikeys/`;
  SETTINGS = "/profile/edit/basic/";
  LOGOUT = "/accounts/logout/";
  SET_LANGUAGE = (languageCode: string) => `/language/set/${languageCode}/`;
  FORUM_HOME = "/forum/";
  FORUM_LATEST = "/forum/topic/latest/";
  FORUM_SUBSCRIBED = "/forum/topic/subscribed";
  SEARCH = "/search/";
  TOP_PICKS = "/explore/top-picks/";
  IOTD = "/iotd/archive/";
  GROUPS = "/groups/";
  TRENDING_ASTROPHOTOGRAPHERS = "/trending-astrophotographers/";
  HELP = "/help/";
  FAQ = "/faq/";
  HELP_API = "/help/api/";
  CONTACT = "/contact/";
  MODERATE_IMAGE_QUEUE = "/moderate/images/";
  MODERATE_SPAM_QUEUE = "/moderate/spam/";
  IOTD_SUBMISSION_QUEUE = "/iotd/submission-queue/";
  IOTD_REVIEW_QUEUE = "/iotd/review-queue/";
  IOTD_JUDGEMENT_QUEUE = "/iotd/judgement-queue/";
}
